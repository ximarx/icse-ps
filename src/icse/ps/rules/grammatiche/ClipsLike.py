'''
Created on 31/mar/2012

@author: Francesco\ Capozzo
'''
from pyparsing import Word, alphanums, alphas, OneOrMore, Forward, nums,\
    Suppress, ZeroOrMore, Group, CharsNotIn, oneOf, Literal
from icse.ps.rules.grammatiche.Grammatica import Grammatica
from icse.ps.rules import condizioni, azioni
from copy import copy

class ClipsLike(Grammatica):
    '''
    Grammatica per file di regole simile alla defrule di clips
    (solo come notazione. Operatori, funzioni e altra roba
    sono di fatto molto differenti)
    '''

    def __init__(self):
        Grammatica.__init__(self)
        self._main = self._prepare_main()
        self._name = "Grammatica Clips-like"
        
    def get_main(self):
        '''
        @return: ParserElement
        '''
        return self._main
    
    def _prepare_main(self):
        '''
        Prepara la grammatica
        '''
        
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
        
        condizione << Group( oneOf(" ".join(condizioni.condizioni())) +  LPAR + Group( operando + ZeroOrMore( ( Suppress(",") + operando) ) ) + RPAR )
        
        azione << Group( oneOf(" ".join(azioni.azioni())) +  LPAR + Group( operando + ZeroOrMore( ( Suppress(",") + operando) ) ) + RPAR )
        
        operatore = Word(alphas, alphanums+"_")
        funzione << Group( operatore +  LPAR + Group( operando + ZeroOrMore( ( Suppress(",") + operando) ) ) + RPAR )
         
        dizionario << Group( Suppress("{") + Group(copy(stringa).setParseAction(lambda t:t[0]) + Suppress(":") + operando) + ZeroOrMore( Suppress(",") + Group(copy(stringa).setParseAction(lambda t:t[0]) + Suppress(":") + operando) ) + Suppress("}") )
        
        congiunzione << Group( oneOf(" ".join(condizioni.congiunzioni())) + LPAR + Group( OneOrMore( congiunzione | condizione ) ) + RPAR )
        
        header = Suppress(DEFRULE_START) + Word(alphas, alphanums + "._-") + Suppress(':')
        separatore = Suppress(DEFRULE_SEPARATOR)
        closer = Suppress(DEFRULE_END)
        
        regola = Group(header + Group(OneOrMore(condizione | congiunzione)) + separatore + Group(OneOrMore(azione)) + closer)
        
        return OneOrMore(regola)
