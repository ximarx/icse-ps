'''
Created on 27/mar/2012

@author: ximarx
'''
from icse.ps.Constraint import Constraint

class ValuesSet(Constraint):
    '''
    Condizione di appartenenza del valore ad una lista
    di valori prefissati
    '''

    def __init__(self, values = None):
        '''
        Constructor
        '''
        if values == None:
            values = []
        
        self._values = values
        
    def to_json(self):
        updated = Constraint.to_json(self)
        updated.update({
                'values' : self._values,
            })
        return updated

    def is_valid(self, value):
        return (self._values.count(value) > 0)