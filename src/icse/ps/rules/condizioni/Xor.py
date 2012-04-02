'''
Created on 30/mar/2012

@author: ximarx
'''
from icse.ps.rules.condizioni.Chain import Chain

class Xor(Chain):
    '''
    Condizione Xor di condizioni
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
        e termina True solo se una sola delle
        subcondizioni e' verificata
        (chiaramente tutte vengono verificate
        '''
        if simboli == None:
            simboli = {}
        return ([x.is_valida(wm, simboli) for x in self._subcondizioni].count(True) == 1)
