'''
Created on 30/mar/2012

@author: ximarx
'''
from icse.ps.rules.funzioni.Funzione import Funzione

class Radice(Funzione):
    '''
    classdocs
    '''
    @staticmethod
    def sign():
        sign = Funzione.sign()
        sign.update({
                'sign': 'radice',
                'minParams': 2,
                'handler': Radice.handler
            })
        return sign
        
    @staticmethod
    def handler(op1, op2):
        return int(int(op1) ** (1.0 / int(op2)))
    
    