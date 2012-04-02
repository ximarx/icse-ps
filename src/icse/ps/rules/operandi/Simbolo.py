'''
Created on 30/mar/2012

@author: ximarx
'''
from icse.ps.rules.operandi.Operando import Operando

class Simbolo(Operando):
    '''
    Rappresenta un simbolo presente nel dizionario di simboli per l'espressione
    '''


    def __init__(self, identificatore):
        '''
        Constructor
        '''
        self._identificatore = "$"+identificatore[1:]
        
    def valuta(self, simboli=None):
        if simboli == None:
            simboli = {}
        if simboli.has_key(self._identificatore):
            return simboli[self._identificatore]
        else:
            raise SimboloSconosciutoError("Simbolo non trovato nel dizionario: "+self._identificatore)
        
    def __str__(self):
        return self._identificatore
        
class SimboloSconosciutoError(Exception):
    pass