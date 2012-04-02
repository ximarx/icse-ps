'''
Created on 30/mar/2012

@author: ximarx
'''
from icse.ps.rules.operandi.Operando import Operando

class Null(Operando):
    '''
    Rappresenta il valore nullo
    '''

    def __init__(self):
        '''
        Constructor
        '''
        
    def valuta(self, simboli=None):
        if simboli == None:
            simboli = {}
        return None
    
    def __str__(self):
        return "NULL"