'''
Created on 27/mar/2012

@author: ximarx
'''
from icse.ps.constraints.Chain import Chain

class XorChain(Chain):
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
        Ammesso esattamente 1 valore True
        fra le condizioni della Chain
        '''
        searchFor = True
        for const in self._constraints:
            if const.is_valid(value):
                if searchFor:
                    searchFor = False
                else:
                    return False

        return (searchFor == False)