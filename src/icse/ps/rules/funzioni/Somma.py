'''
Created on 30/mar/2012

@author: ximarx
'''
from icse.ps.rules.funzioni.Funzione import Funzione

class Somma(Funzione):
    '''
    classdocs
    '''
    @staticmethod
    def sign():
        sign = Funzione.sign()
        sign.update({
                'sign': 'somma',
                'minParams': 2,
                'handler': Somma.handler
            })
        return sign
        
    @staticmethod
    def handler(op1, op2):
        return (int(op1) + int(op2))
    
    