'''
Created on 27/mar/2012

@author: ximarx
'''
from icse.ps.Constraint import Constraint

class Chain(Constraint):
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
        self._constraints = [constraint for constraint in constraints if isinstance(constraint, Constraint)]
            
        
    def append_constraint(self, constraint):
        '''
        Aggiunge una nuova condizione alla lista
        Usa fluent interface
        
        @param constraint: icse.ps.Constraint.Constraint
        @return: icse.ps.constraints.AndChain.AndChain
        '''
        if isinstance(constraint, Constraint):
            self._constraints.append(constraint)
            
        return self
    
    def to_json(self):
        updated = Constraint.to_json(self)
        updated.update({
                'constraints' : [constraint.to_json() for constraint in self._constraints]
            })
        return updated
    
