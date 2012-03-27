'''
Created on 27/mar/2012

@author: ximarx
'''
from icse.ps.constraints.Chain import Chain

class OrChain(Chain):
    '''
    Rappresenta una And Chain di condizioni
    sugli attributi
    '''

    def __init__(self, constraints = []):
        '''
        Constructor
        '''
        Chain.__init__(self, constraints) 
    
    def is_valid(self, value):
        '''
        La chain e' vera non appena la prima
        condizione vera e' trovata nella lista
        '''
        for const in self._constraints:
            if const.is_valid(value):
                return True
            
        return False
    