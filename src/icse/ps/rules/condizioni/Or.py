'''
Created on 30/mar/2012

@author: ximarx
'''
from icse.ps.rules.condizioni.Chain import Chain

class Or(Chain):
    '''
    Condizione Or di condizioni
    '''

    def __init__(self, subcondizioni = None):
        '''
        Inizializza la chain
        '''
        if subcondizioni == None:
            subcondizioni = []
        Chain.__init__(self, subcondizioni)
        
    def is_valida(self, wm, simboli=None):
        '''
        Controlla tutte le subcondizioni
        e termina il controllo alla prima
        subcondizione verificata
        '''
        if simboli == None:
            simboli = {}
            
        for condizione in self._subcondizioni:
            if condizione.is_valida(wm, simboli):
                return True
            
        return False
    
    def __str__(self):
        return "( " + " oppure ".join([str(x) for x in self._subcondizioni]) + " )"