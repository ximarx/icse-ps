'''
Created on 30/mar/2012

@author: Francesco Capozzo
'''
from icse.ps.rules.condizioni.Condizione import Condizione

class Not(Condizione):
    '''
    Inverte una condizione
    '''


    def __init__(self, subcondizione):
        '''
        Constructor
        '''
        if not isinstance(subcondizione, Condizione):
            raise TypeError("Atteso tipo Condizione, passato: " + str(subcondizione.__class__.__name__))
        
        '''
        @var self._subcondizione: Condizione
        '''
        self._subcondizione = subcondizione
        
        
    def is_valida(self, wm, simboli=None):
        if simboli == None:
            simboli = {}
        return not self._subcondizione.is_valida(wm, simboli)
    
    def __str__(self):
        return "not ( "+str(self._subcondizione)+" )"
