'''
Created on 05/apr/2012

@author: Francesco Capozzo
'''
from icse.ps.rules.Regola import Regola

class Algoritmo(object):
    '''
    Classe base per gli algoritmi per la risoluzione
    '''

    def __init__(self, wmemory, agenda):
        '''
        Constructor
        '''
        self._wmemory = wmemory
        self._agenda = agenda
        self._options = {}
        self._optimizations = {}
        self._lambdacond = None
        
    def set_options(self, options = None):
        '''
        '''
        if options == None:
            options = {}
            
        self._options.update(options)
        
    def set_optimizations(self, optz = None):
        if optz == None:
            optz = {}
        self._optimizations.update(optz)
        
    def _get_option(self, key, default = None):
        if self._options.has_key(key) and self._options[key] != None:
            return self._options[key]
        else:
            return default

    def _get_optimization(self, key, default = None):
        if self._optimizations.has_key(key) and self._optimizations[key] != None:
            return self._optimizations[key]
        else:
            return default
        
    def execute(self, goal):
        raise NotImplementedError("Metodo astratto")
            
    def _prepare_lamda(self, goal):
        if isinstance(goal, Regola):
            self._lambdacond = lambda t:goal.is_valida(t)
        else:
            self._lambdacond = lambda t:(goal == t)
        
    def _is_goal(self, wmemory):
        assert callable(self._lambdacond),\
            "Funzione Lamda non ancora preparata"
        return self._lambdacond(wmemory)