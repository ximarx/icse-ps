'''
Created on 31/mar/2012

@author: Francesco Capozzo
'''

class Grammatica:
    '''
    Classe base per la rappresentazione di una grammatica
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self._bnf = "BNF non specificato"
        self._main = None
        self._name = "Grammatica astratta"

    def get_main(self):
        '''
        Restituisce un oggetto pyparsing rappresentante
        l'entry point di una grammatica (la definizione principale)
        '''
        return self._main
    
    def get_bnf(self):
        return self._bnf
    
    def get_name(self):
        return self._name