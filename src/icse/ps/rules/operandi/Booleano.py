'''
Created on 30/mar/2012

@author: ximarx
'''
from icse.ps.rules.operandi.Operando import Operando

class Booleano(Operando):
    '''
    Rappresenta un valore booleano
    '''


    def __init__(self, valore):
        '''
        Constructor
        '''
        valore = (valore == "True" or valore == True)
        self._valore = valore
        
    def valuta(self, simboli={}):
        return self._valore
    
    def __str__(self):
        return str(self._valore)