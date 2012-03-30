'''
Created on 30/mar/2012

@author: ximarx
'''
from icse.ps.rules.condizioni.Condizione import Condizione

class Chain(Condizione):
    '''
    Condizione rappresentante una lista di condizioni
    '''


    def __init__(self, subcondizioni = []):
        '''
        Constructor
        '''
        # filtra le subcondizioni accettando solo
        # condizioni
        self._subcondizioni = [x for x in subcondizioni if isinstance(x, Condizione)]
        
    def aggiungi(self, subcondizione):
        if isinstance(subcondizione, Condizione) :
            self._subcondizioni.append(subcondizione)
