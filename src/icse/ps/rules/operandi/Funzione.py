'''
Created on 30/mar/2012

@author: ximarx
'''
from icse.ps.rules.operandi.Operando import Operando
from icse.ps.rules.funzioni.Proxy import Proxy

class Funzione(Operando):
    '''
    Rappresenta una funzione valutabile
    '''


    def __init__(self, nome, parametri = []):
        '''
        Constructor
        '''
        self._nome = nome
        self._parametri = [x for x in parametri if isinstance(x, Operando)]
        
    def valuta(self, simboli={}):
        op_valutati = [x.valuta(simboli) for x in self._parametri]
        return Proxy.call(self._nome, op_valutati)
        
        
    