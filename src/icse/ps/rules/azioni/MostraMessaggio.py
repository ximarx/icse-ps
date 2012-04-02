'''
Created on 31/mar/2012

@author: Francesco Capozzo
'''
from icse.ps.rules.azioni.Azione import Azione
from icse.ps.rules.operandi.Operando import Operando

class MostraMessaggio(Azione):
    '''
    Ritratta un fatto dalla WorkingMemory
    '''

    def __init__(self, messaggio ):
        '''
        Constructor
        '''
        assert isinstance(messaggio, Operando) or isinstance(messaggio, str), \
            "Atteso messaggio di tipo Operando o string, fornito: "+str(type(messaggio))
            
        self._messaggio = messaggio
        
    def esegui(self, wm, simboli, agenda):
        '''
        Esegue la modifica di un attributo di un fatto
        '''
        '''chiamo il metodo base per il controllo dei parametri'''
        Azione.esegui(self, wm, simboli, agenda)
        
        '''risolvo messaggio'''
        vmessaggio = self._messaggio
        if isinstance(vmessaggio, Operando):
            vmessaggio = vmessaggio.valuta(simboli)
            
        assert isinstance(vmessaggio, "".__class__), \
            "Atteso messaggio di tipo string dopo la valutazione, ottenuto: "+str(type(vmessaggio))

        print vmessaggio
        
    def __str__(self):
        return " ".join([
                'mostra il messaggio',
                str(self._messaggio)
            ])
