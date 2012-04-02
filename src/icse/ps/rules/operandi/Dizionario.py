'''
Created on 31/mar/2012

@author: Francesco\ Capozzo
'''
from icse.ps.rules.operandi.Operando import Operando

class Dizionario(Operando):
    '''
    Rappresenta un dizionario di valori
    '''


    def __init__(self, valori):
        '''
        Constructor
        '''
        self._valori = dict(valori)
        
    def valuta(self, simboli=None):
        if simboli == None:
            simboli = {}
        return dict([(key, val.valuta(simboli)) for (key,val) in self._valori.items()])
    
    def __str__(self):
        return str(dict([(str(x), str(y)) for (x,y) in self._valori.items() ]))