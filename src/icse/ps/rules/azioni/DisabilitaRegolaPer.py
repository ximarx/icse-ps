'''
Created on 31/mar/2012

@author: Francesco Capozzo
'''
from icse.ps.rules.azioni.Azione import Azione
from icse.ps.rules.operandi.Operando import Operando

class DisabilitaRegolaPer(Azione):
    '''
    Ritratta un fatto dalla WorkingMemory
    '''

    def __init__(self, regola, turni ):
        '''
        Constructor
        '''
        assert isinstance(regola, Operando) or isinstance(regola, "".__class__), \
            "Atteso regola di tipo Operando o string, fornito: "+str(type(regola))
            
        assert isinstance(turni, Operando) or isinstance(turni, int), \
            "Atteso turni di tipo Operando o int, fornito: "+str(type(turni))
            
        self._regola = regola
        self._turni = turni
        
    def esegui(self, wm, simboli, agenda):
        '''
        Esegue la modifica di un attributo di un fatto
        '''
        '''chiamo il metodo base per il controllo dei parametri'''
        Azione.esegui(self, wm, simboli, agenda)
        
        '''risolvo regola'''
        vregola = self._regola
        if isinstance(vregola, Operando):
            vregola = vregola.valuta(simboli)

        '''risolvo turni'''
        vturni = self._turni
        if isinstance(vturni, Operando):
            vturni = vturni.valuta(simboli)
            
        assert isinstance(vregola, "".__class__), \
            "Atteso regola di tipo string dopo la valutazione, ottenuto: "+str(type(vregola))

        assert isinstance(vturni, int), \
            "Atteso turni di tipo int dopo la valutazione, ottenuto: "+str(type(vturni))

        '''tutto e' pronto per l'esecuzione'''

        #TODO riabilitare quando agenda sara' pronto
        agenda.set_penality(vregola, vturni)
        
    def __str__(self):
        return " ".join([
                'disabilita la regola',
                str(self._regola),
                'per',
                str(self._turni),
                'turni'
            ])
