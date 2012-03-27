'''
Created on 27/mar/2012

@author: ximarx
'''
from icse.ps.Constraint import Constraint

class Not(Constraint):
    '''
    Inverte una condizione
    '''

    def __init__(self, constraint):
        '''
        Constructor
        '''
        self._constraint = constraint
        
    def to_json(self):
        updated = Constraint.to_json(self)
        updated.update({
                'constraint' : self._constraint.to_json()
            })
        return updated

    def is_valid(self, value):
        '''
        Inverte il risultato della
        sub-condizione, qualunque essa sia
        '''
        return (not self._constraint.is_valid(value))