'''
Created on 31/mar/2012

@author: Francesco Capozzo
'''
from icse.ps.rules.azioni.Azione import Azione
from icse.ps.rules.operandi.Operando import Operando
from icse.ps.Fact import Fact

class Ritratta(Azione):
    '''
    Ritratta un fatto dalla WorkingMemory
    '''

    def __init__(self, fatto):
        '''
        Constructor
        '''
        assert isinstance(fatto, Operando) or isinstance(fatto, Fact), \
            "Atteso fatto di tipo Operando o Fact, fornito: "+str(type(fatto))
            
        self._fatto = fatto
        
    def esegui(self, wm, simboli, agenda):
        '''
        Esegue la modifica di un attributo di un fatto
        '''
        '''chiamo il metodo base per il controllo dei parametri'''
        Azione.esegui(self, wm, simboli, agenda)
        
        '''risolvo fatto'''
        vfatto = self._fatto
        if isinstance(vfatto, Operando):
            vfatto = vfatto.valuta(self, simboli)
            
        '''tutto e' pronto per l'esecuzione'''
        assert isinstance(vfatto, Fact), \
            "Atteso fatto di tipo Fact dopo la valutazione, ottenuto: "+str(type(vfatto))
             
        wm.retract_fact(vfatto)
        

