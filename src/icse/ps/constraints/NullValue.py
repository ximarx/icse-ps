'''
Created on 27/mar/2012

@author: ximarx
'''
from icse.ps.Constraint import Constraint

class NullValue(Constraint):
    '''
    Rappresenta la condizione di valore Nullo
    (piu che altro utile legata tramite chain
    ad altri tipi di condizioni come ValuesSet o Range)
    '''

    def __init__(self):
        '''
        Constructor
        '''
        
    def is_valid(self, value):
        return (value == '' or value == None)