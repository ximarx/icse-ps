from pyparsing import Word, alphanums, alphas, OneOrMore, Forward, nums,\
    Suppress, ZeroOrMore, Group, CharsNotIn, oneOf, Literal
import os
from copy import copy
from icse.ps.rules.Regola import Regola
from icse.ps.rules.operandi.Simbolo import Simbolo
from icse.ps.rules.operandi.Stringa import Stringa
from icse.ps.rules.operandi.Null import Null
from icse.ps.rules.operandi.Numero import Numero
from icse.ps.rules.operandi.Booleano import Booleano
from icse.ps.rules.operandi.Dizionario import Dizionario
from icse.ps.rules.operandi.Funzione import Funzione
from icse.ps.rules import condizioni, azioni


DEFRULE_START = "defrule"
DEFRULE_END = ":defrule"
DEFRULE_SEPARATOR = "==>"
LPAR = Suppress("(")
RPAR = Suppress(")")

variabile = Word('$', alphanums+"_-")\
    .setParseAction(lambda t:('var', t[0]))
    
stringa = (Suppress("'") + CharsNotIn("'") + Suppress("'") ^ \
            Suppress('"') + CharsNotIn('"') + Suppress('"'))\
    .setParseAction(lambda t:('string', str(t[0])))
    

funzione = Forward()\
    .setParseAction(lambda t:('function', t[0][0], t[0][1][:]))

dizionario = Forward()\
    .setParseAction(lambda t:('dict', [(x[0],x[1]) for x in t[0]] ))
    
booleano = oneOf("True False")\
    .setParseAction(lambda t:('bool', bool(t[0])))

intero = Word(nums)\
    .setParseAction(lambda t:('int',int(t[0])))
    
null = Literal("NULL")\
    .setParseAction(lambda t:('null', None))
    
congiunzione = Forward()\
    .setParseAction(lambda t:('conj', t[0][0], t[0][1][:]))

condizione = Forward()\
    .setParseAction(lambda t:('condition', t[0][0], t[0][1][:]))

azione = Forward()\
    .setParseAction(lambda t:('action', t[0][0], t[0][1][:]))


operando = (variabile | stringa | congiunzione | condizione | funzione | null | intero | booleano | dizionario ) 

# da caricare tramite il package
#condizioni_ = ['esiste', 'uguale', 'minore', 'maggiore', 'minore-uguale', 'maggiore-uguale']
condizione << Group( oneOf(" ".join(condizioni.condizioni())) +  LPAR + Group( operando + ZeroOrMore( ( Suppress(",") + operando) ) ) + RPAR )

# da caricare tramite il package
#azioni_ = ['asserisci', 'cambiaFatto', 'ritratta', 'disabilitaRegolaPer']
azione << Group( oneOf(" ".join(azioni.azioni())) +  LPAR + Group( operando + ZeroOrMore( ( Suppress(",") + operando) ) ) + RPAR )

operatore = Word(alphas, alphanums+"_")
funzione << Group( operatore +  LPAR + Group( operando + ZeroOrMore( ( Suppress(",") + operando) ) ) + RPAR )
 
dizionario << Group( Suppress("{") + Group(copy(stringa).setParseAction(lambda t:t[0]) + Suppress(":") + operando) + ZeroOrMore( Suppress(",") + Group(copy(stringa).setParseAction(lambda t:t[0]) + Suppress(":") + operando) ) + Suppress("}") )

# da caricare tramite il package
#congiunzioni = ["and", "or", "xor", "not"]
congiunzione << Group( oneOf(" ".join(condizioni.congiunzioni())) + LPAR + Group( OneOrMore( congiunzione | condizione ) ) + RPAR )

header = Suppress(DEFRULE_START) + Word(alphas, alphanums + "._-") + Suppress(':')
separatore = Suppress(DEFRULE_SEPARATOR)
closer = Suppress(DEFRULE_END)

regola = Group(header + Group(OneOrMore(condizione | congiunzione)) + separatore + Group(OneOrMore(azione)) + closer)

grammar = OneOrMore(regola)

basePath = os.getcwd()+"/../../../.."

result = grammar.parseFile( basePath + "/games/8/rules.txt" , True)

def interpreta_operazione(o):
    '''
    '''
    tipo = o[0]
    obj = None
    #ELEMENTARI (non ricorsivi)
    if tipo == 'var':
        obj = Simbolo(o[1])
    elif tipo == 'string':
        obj = Stringa(o[1])
    elif tipo == 'null':
        obj = Null()
    elif tipo == 'int':
        obj = Numero(o[1])
    elif tipo == 'bool':
        obj = Booleano(o[1])
    #CHAINS
    elif tipo == 'dict':
        obj = Dizionario(dict([(x,interpreta_operazione(y)) for (x,y) in o[1]]))
    elif tipo == 'function':
        obj = Funzione(o[1], [interpreta_operazione(x) for x in o[2]])
    elif tipo == 'condition':
        obj = condizioni.factory(o[1], [interpreta_operazione(x) for x in o[2]])
    elif tipo == 'conj':
        obj = condizioni.factory(o[1], [[interpreta_operazione(x) for x in o[2]]])
    elif tipo == 'action':
        obj = azioni.factory(o[1], [interpreta_operazione(x) for x in o[2]])
    else:
        obj = Null()
        
    return obj

for i in result:
    print "Regola: ",i[0]
    print "Precondizioni:"
    for j in i[1]:
        print "\t",j
    print "Attuatori:"
    for j in i[2]:
        print "\t",j
    print

    regola = Regola(
                i[0],
                [interpreta_operazione(o) for o in i[1]],
                [interpreta_operazione(o) for o in i[2]]
        )
    
    print str(regola)

    
    




"""
result = []

teststr = '''
defrule sposta-vuoto-su:
    esiste( $X, 'Cella', 
        uguale( attributo($X, 'valore'), NULL )
    ) 
    esiste( $Y, 'Cella', 
        uguale( attributo($Y, 'y'), sottrazione( attributo($X, 'y'), 1) ) 
    )
    or(
        uguale( attributo($X, 'x'), attributo($Y, 'x') )
        uguale( attributo($Y, 'x'), attributo($X, 'x') )
    )
==>
    asserisci("fatto-n", 'Cella', {
        'attr1': 'valore',
        'attr2': funzione(1,1),
        'attr3': NULL
    })
    cambiaFatto($Y, 'y', somma( attributo($Y, 'y'), 1))
    disabilitaRegolaPer('sposta-vuoto-giu', 1)
:defrule
'''

result = grammar.parseString(teststr, True)

for i in result:
    print "Regola: ",i[0]
    print "Precondizioni:"
    for j in i[1]:
        print "\t",j
    print "Attuatori:"
    for j in i[2]:
        print "\t",j
    print

    regola = Regola(
                i[0],
                [interpreta_operazione(o) for o in i[1]],
                [interpreta_operazione(o) for o in i[2]]
        )
    
    print str(regola)



"""























