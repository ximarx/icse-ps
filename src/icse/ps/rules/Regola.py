'''
Created on 30/mar/2012

@author: ximarx
'''

class Regola:
    '''
    Rappresenta una regola
    '''


    def __init__(self, nome, condizioni, azioni, simboli = {}):
        '''
        Constructor
        '''
        self._nome = nome
        self._condizioni = condizioni
        self._azioni = azioni
        self._simboli = simboli
        
    def is_valida(self, wm):
        '''
        controlla se la regola e' applicabile
        nello stato attuale della wm
        '''
        
        for condizione in self._condizioni:
            if not condizione.is_valida(wm, self._simboli):
                #la prima condizione non soddisfatta determina
                #l'arresto della verifica
                return False
            
        return True
    
    def attiva(self, wm, agenda):
        '''
        attiva una regola
        '''
        for azione in self._azioni:
            azione.esegui(wm, self._simboli, agenda)
        
    def __str__(self):
        return "Regola: "+self._nome+"\n"\
            "\tSe si verifica che:\n\t\t" + "\n\t\t".join([str(x) for x in self._condizioni])+"\n"+\
            "\tAllora:\n\t\t" + "\n\t\t".join([str(x) for x in self._azioni])