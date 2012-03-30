'''
Created on 30/mar/2012

@author: ximarx
'''
from icse.ps.rules.funzioni.Funzione import Funzione

class Potenza(Funzione):
    '''
    classdocs
    '''
    @staticmethod
    def sign():
        sign = Funzione.sign()
        sign.update({
                'sign': 'potenza',
                'minParams': 2,
                'handler': Potenza.handler
            })
        return sign
        
    @staticmethod
    def handler(op1, op2):
        return (int(op1) ** int(op2))
    
    