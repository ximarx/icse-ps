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


    def __init__(self, nome, parametri = None):
        '''
        Constructor
        '''
        if parametri == None:
            parametri = []
        self._nome = nome
        self._parametri = [x for x in parametri if isinstance(x, Operando)]
        
    def valuta(self, simboli=None):
        if simboli == None:
            simboli = {}
        op_valutati = [x.valuta(simboli) for x in self._parametri]
        return Proxy.call(self._nome, op_valutati)
    
    def __str__(self):
        return self._nome + "(" + ", ".join([str(x) for x in self._parametri]) + ")"
        
        
    