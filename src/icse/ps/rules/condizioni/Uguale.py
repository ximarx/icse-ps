'''
Created on 30/mar/2012

@author: ximarx
'''
from icse.ps.rules.condizioni.Condizione import Condizione
from icse.ps.rules.operandi.Operando import Operando

class Uguale(Condizione):
    '''
    Condizione di uguaglianza
    '''

    def __init__(self, operando1, operando2):
        '''
        Constructor
        '''
        self._op1 = operando1
        self._op2 = operando2
        
    def is_valida(self, wm, simboli={}):
        if isinstance(self._op1, Operando):
            vop1 = self._op1.valuta(simboli)
        if isinstance(self._op1, Operando):
            vop2 = self._op2.valuta(simboli)
        
        return (vop1 == vop2)
    
    def __str__(self):
        '''
        Rappresenta la condizione come stringa nella forma:
            "(operando1 uguale operando2)"
        '''
        return " ".join([
                "(",
                    str(self._op1),
                    'uguale',
                    str(self._op2),
                ")"
            ])