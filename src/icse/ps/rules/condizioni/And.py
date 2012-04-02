'''
Created on 30/mar/2012

@author: ximarx
'''
from icse.ps.rules.condizioni.Chain import Chain

class And(Chain):
    '''
    Condizione And di condizioni
    '''


    def __init__(self, subcondizioni = None):
        '''
        Inizializza la chain
        '''
        if subcondizioni == None:
            subcondizioni = []
        Chain.__init__(self, subcondizioni)
        
    def is_valida(self, wm, simboli = None):
        '''
        Controlla tutte le subcondizioni
        e termina il controllo alla prima
        subcondizione non verificata
        '''
        
        if simboli == None:
            simboli = {}
        
        for condizione in self._subcondizioni:
            if not condizione.is_valida(wm, simboli):
                return False
            
        return True
    
    def __str__(self):
        return " e ".join([str(x) for x in self._subcondizioni])