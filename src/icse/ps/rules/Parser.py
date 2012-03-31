'''
Created on 31/mar/2012

@author: Francesco Capozzo
'''
from pyparsing import ParseResults
from icse.ps.rules.Regola import Regola
from icse.ps.rules.operandi.Simbolo import Simbolo
from icse.ps.rules.operandi.Stringa import Stringa
from icse.ps.rules.operandi.Null import Null
from icse.ps.rules.operandi.Numero import Numero
from icse.ps.rules.operandi.Booleano import Booleano
from icse.ps.rules.operandi.Dizionario import Dizionario
from icse.ps.rules.operandi.Funzione import Funzione
from icse.ps.rules import condizioni, azioni
from icse.ps.rules.grammatiche.Grammatica import Grammatica

class Parser:
    '''
    Parser di regole
    '''

    def __init__(self, grammatica = None):
        '''
        Constructor
        '''
        self._grammatica = None
        if grammatica != None :
            self.set_grammatica(grammatica)
            
    def set_grammatica(self, grammatica):
        assert isinstance(grammatica, Grammatica)
        self._grammatica = grammatica
        return self
        
    def parse(self, filename):
        assert isinstance(self._grammatica, Grammatica)
        results = self._grammatica.get_main().parseFile(filename)
        return self._interpreta(results)
        
    def _interpreta(self, results):
        assert isinstance(results, ParseResults) or isinstance(results, list)
        
        return [Regola(
                       rule[0],
                       [self._interpreta_atomo(cond) for cond in rule[1]],
                       [self._interpreta_atomo(cond) for cond in rule[2]]
                    )
                    for rule in results]
        
    def _interpreta_atomo(self, atomo):
        
        tipo = atomo[0]
        obj = None
        #ELEMENTARI (non ricorsivi)
        if tipo == 'var':
            obj = Simbolo(atomo[1])
        elif tipo == 'string':
            obj = Stringa(atomo[1])
        elif tipo == 'null':
            obj = Null()
        elif tipo == 'int':
            obj = Numero(atomo[1])
        elif tipo == 'bool':
            obj = Booleano(atomo[1])
        #CHAINS
        elif tipo == 'dict':
            obj = Dizionario(dict([(x,self._interpreta_atomo(y)) for (x,y) in atomo[1]]))
        elif tipo == 'function':
            obj = Funzione(atomo[1], [self._interpreta_atomo(x) for x in atomo[2]])
        elif tipo == 'condition':
            obj = condizioni.factory(atomo[1], [self._interpreta_atomo(x) for x in atomo[2]])
        elif tipo == 'conj':
            obj = condizioni.factory(atomo[1], [[self._interpreta_atomo(x) for x in atomo[2]]])
        elif tipo == 'action':
            obj = azioni.factory(atomo[1], [self._interpreta_atomo(x) for x in atomo[2]])
        else:
            obj = Null()
            
        return obj
        
        