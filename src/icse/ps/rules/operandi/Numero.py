'''
Created on 30/mar/2012

@author: ximarx
'''
from icse.ps.rules.operandi.Operando import Operando

class Numero(Operando):
    '''
    Rappresenta un valore numerico (intero positivo)
    '''

    def __init__(self, valore):
        '''
        Constructor
        '''
        self._valore = int(valore)
        
    def valuta(self, simboli=None):
        if simboli == None:
            simboli = {}
        return self._valore
    
    def __str__(self):
        return str(self._valore)