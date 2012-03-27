'''
Created on 27/mar/2012

@author: ximarx
'''
from icse.ps.Constraint import Constraint

class Range(Constraint):
    '''
    Impone un range di valori interi validi
    nei quali deve cadere il valore
    '''


    def __init__(self, minVal, maxVal):
        '''
        Constructor
        '''
        self._min = minVal
        self._max = maxVal
        
    def to_json(self):
        updated = Constraint.to_json(self)
        updated.update({
                'minVal' : self._min,
                'maxVal' : self._max
            })
        return updated
    
    def is_valid(self, value):
        '''
        Controlla che il valore sia compreso nel range
        '''
        return (self._min <= value and value <= self._max)
        