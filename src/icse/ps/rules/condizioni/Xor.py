'''
Created on 30/mar/2012

@author: ximarx
'''
from icse.ps.rules.condizioni.Chain import Chain

class Xor(Chain):
    '''
    Condizione Xor di condizioni
    '''


    def __init__(self, subcondizioni = []):
        '''
        Inizializza la chain
        '''
        Chain.__init__(self, subcondizioni)
        
    def is_valida(self, wm, simboli={}):
        '''
        Controlla tutte le subcondizioni
        e termina True solo se una sola delle
        subcondizioni e' verificata
        (chiaramente tutte vengono verificate
        '''
        return ([x.is_valida(wm, simboli) for x in self._subcondizioni].count(True) == 1)
