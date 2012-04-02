'''
Created on 30/mar/2012

@author: ximarx
'''

class Condizione():
    '''
    Classe base di una condizione
    '''


    def __init__(self):
        '''
        Inizializza la condizione
        '''
        
    def is_valida(self, wm, simboli = None):
        if simboli == None:
            simboli = {}
        return True
    
    def __str__(self):
        return "vero"