'''
Created on 31/mar/2012

@author: Francesco\ Capozzo
'''
from icse.ps.rules.azioni.Azione import Azione
from icse.ps.rules.operandi.Operando import Operando
from icse.ps.Fact import Fact

class CambiaFatto(Azione):
    '''
    Permette la modifica di un attributo
    di un Fact nella WorkingMemory
    '''

    def __init__(self, fatto, attributo, valore):
        '''
        Constructor
        '''
        assert isinstance(fatto, Operando) or isinstance(fatto, Fact), \
            "Atteso fatto di tipo Operando o Fact, fornito: "+str(type(fatto))
        assert isinstance(attributo, Operando) or isinstance(attributo, "".__class__), \
            "Atteso attributo di tipo Operando o string, fornito: "+str(type(attributo))
        assert isinstance(valore, Operando), \
            "Atteso valore di tipo Operando, fornito: "+str(type(valore))
            
        self._fatto = fatto
        self._attributo = attributo
        self._valore = valore
        
    def esegui(self, wm, simboli, agenda):
        '''
        Esegue la modifica di un attributo di un fatto
        '''
        '''chiamo il metodo base per il controllo dei parametri'''
        Azione.esegui(self, wm, simboli, agenda)
        
        '''risolvo il reale valore del fatto se operando (simbolo quasi sicuramente)'''
        vfatto = self._fatto
        if isinstance(vfatto, Operando):
            vfatto = vfatto.valuta(simboli)
        
        '''risolvo il reale valore del attributo se operando'''
        vattributo = self._attributo
        if isinstance(vattributo, Operando):
            vattributo = vattributo.valuta(simboli)
            
        '''risolvo il reale valore del valore se operando'''
        vvalore = self._valore
        if isinstance(vvalore, Operando):
            vvalore = vvalore.valuta(simboli)
            
        '''tutto e' pronto per l'esecuzione'''
        assert isinstance(vfatto, Fact), \
            "Atteso Fatto dopo la valutazione, ottenuto: "+str(type(vfatto))
             
        vfatto[vattributo] = vvalore

    def __str__(self):
        return " ".join([
                "modifica il fatto",
                str(self._fatto),
                "cambiando l'attributo",
                str(self._attributo),
                "in",
                str(self._valore)
            ])
