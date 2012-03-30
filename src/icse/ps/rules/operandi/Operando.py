'''
Created on 30/mar/2012

@author: Francesco Capozzo
'''

class Operando:
    '''
    Rappresentazione di un operando
    '''


    def __init__(self):
        '''
        Constructor
        '''
        raise NotImplementedError("Metodo astratto")
        
    def valuta(self, simboli = {}):
        '''
        valuta l'espressione utilizzando la
        tabella dei simboli se necessario
        '''
        raise NotImplementedError("Metodo astratto")
    
    def __str__(self):
        raise NotImplementedError("Metodo astratto")
    
    