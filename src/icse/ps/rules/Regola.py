'''
Created on 30/mar/2012

@author: ximarx
'''

class Regola:
    '''
    Rappresenta una regola
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self._condizioni = []
        self._azioni = []
        self._simboli = {}
        
    def is_valida(self, wm):
        '''
        controlla se la regola e' applicabile
        nello stato attuale della wm
        '''
        
        self._simboli = {}
        
        for condizione in self._condizioni:
            if not condizione.is_valida(wm, self._simboli):
                #la prima condizione non soddisfatta determina
                #l'arresto della verifica
                return False
            
        return True
    
    def attiva(self, wm, agenda):
        '''
        attiva una regola
        '''
        for azione in self._azioni:
            azione.esegui(wm, self._simboli, agenda)
        