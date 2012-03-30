from pyparsing import Word, alphanums, alphas, OneOrMore, Forward, nums,\
    Suppress, ZeroOrMore, Group, CharsNotIn, oneOf
import os

DEFRULE_START = "defrule"
DEFRULE_END = ":defrule"
LPAR = Suppress("(")
RPAR = Suppress(")")

variabile = Word('$', alphanums+"_-")
stringa = Suppress("'") + CharsNotIn("'") + Suppress("'") ^ \
            Suppress('"') + CharsNotIn('"') + Suppress('"')
funzione = Forward()
booleano = oneOf("True False")
operando = (variabile | stringa | funzione | "NULL" | Word(nums) | booleano ) 
operatore = Word(alphas, alphanums+"_")
funzione << Group( operatore +  LPAR + Group( operando + ZeroOrMore( ( Suppress(",") + operando) ) ) + RPAR ) 


conjuctions = ["and", "or", "xor", "not"]
congiunzione = Forward()
congiunzione << Group( oneOf(" ".join(conjuctions)) + LPAR + Group( OneOrMore( funzione | congiunzione ) ) + RPAR )

header = Suppress('defrule') + Word(alphas, alphanums + "._-") + Suppress(':')
separatore = Suppress("==>")
closer = Suppress(':defrule')

regola = Group(header + Group(OneOrMore(funzione | congiunzione)) + separatore + Group(OneOrMore(funzione)) + closer)

grammar = OneOrMore(regola)

basePath = os.getcwd()+"/../../../.."

result = grammar.parseFile( basePath + "/games/8/rules.txt" , True)

for i in result:
    print "Regola: ",i[0]
    print "Precondizioni:"
    for j in i[1]:
        print "\t",j
    print "Attuatori:"
    for j in i[2]:
        print "\t",j
    print

#rule = DEFRULE_START + rulename + ":" + OneOrMore(condition) + "==>" + OneOrMore(action) + DEFRULE_END 





























