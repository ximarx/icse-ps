'''
Created on 30/mar/2012

@author: ximarx
'''
from icse.ps.rules.operandi.Operando import Operando

class Stringa(Operando):
    '''
    Rappresenta una stringa
    '''

    def __init__(self, valore):
        '''
        Constructor
        '''
        self._valore = str(valore)
        
    def valuta(self, simboli={}):
        return self._valore
    
    def __str__(self):
        return '"'+self._valore+'"'
    