'''
Created on 31/mar/2012

@author: Francesco Capozzo
'''
from icse.ps.wm.WorkingMemory import WorkingMemory
from icse.ps.Agenda import Agenda

class Azione(object):
    '''
    Azione base che compone
    la parte destra di una regola
    '''

    def __init__(self):
        '''
        Constructor
        '''
        
    def esegui(self, wm, simboli, agenda):
        '''
        Esegue i controlli base sui parametri
        '''
        assert isinstance(wm, WorkingMemory), "Atteso wm di tipo WorkingMemory, fornito: "+str(type(wm))
        assert isinstance(simboli, dict), "Atteso simboli di tipo dict, fornito: "+str(type(simboli))
        assert isinstance(agenda, Agenda), "Atteso agenda di tipo Agenda, fornito: "+str(type(agenda))
        
    def __str__(self):
        return "azione generica"
        
        