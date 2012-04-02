'''
Created on 27/mar/2012

@author: ximarx
'''
from icse.ps.constraints.Chain import Chain

class AndChain(Chain):
    '''
    Rappresenta una And Chain di condizioni
    sugli attributi
    '''

    def __init__(self, constraints = None):
        '''
        Constructor
        '''
        if constraints == None:
            constraints = []
        Chain.__init__(self, constraints)
            
    def is_valid(self, value):
        '''
        Tutte le subcondizioni della chain
        devono essere valide affinche la chain
        sia valida
        '''
        return ([const.is_valid(value) for const in self._constraints].count(False) > 0)
        
