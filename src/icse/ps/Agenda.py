'''
Created on 31/mar/2012

@author: Francesco Capozzo
'''
from icse.ps.rules.Regola import Regola
from icse.ps.wm.WorkingMemory import WorkingMemory

class Agenda:
    '''
    classdocs
    '''


    def __init__(self, regole = None):
        '''
        Constructor
        '''
        if regole == None:
            regole = []
        self._regole = dict([(x.get_nome(),x) for x in regole if isinstance(x, Regola)])
        self._penality = {}
        
    def set_penality(self, regola, turni):
        '''
        Imposta una penality all'esecuzione di una regola,
        impedendo l'esecuzione della regola nei successivi n turni
        recognize-act
        '''
        assert isinstance(regola, str) or isinstance(regola, Regola),\
            "Attesa regola di tipo str o regola, fornito: "+str(type(regola))
        assert isinstance(turni, int),\
            "Atteso turni di tipo int, fornito"+str(type(turni))
            
        if isinstance(regola, Regola):
            regola = regola.get_nome()
            
        if not self._regole.has_key(regola):
            raise RegolaNonTrovataError("Regola non in agenda: "+str(regola))
        
        self._penality[regola] = turni
            
        return self
    
    def do_decrease_penalities(self):
        self._penality = dict([(k, v-1) for (k,v) in self._penality.items() if v > 1])
        return self
    
    def set_regola(self, regola):
        assert isinstance(regola, Regola),\
            "Atteso regola di tipo Regola, fornito: "+str(type(regola))
            
        self._regole[regola.get_nome()] = regola
        
    def remove_regola(self, regola):
        assert isinstance(regola, Regola) or isinstance(regola, str),\
            "Atteso regola di tipo Regola o str, fornito: "+str(type(regola))
            
        # faccio doppia conversione str->regola->str per uniformare i casi in cui
        # e' str e Regola
        if isinstance(regola, str):
            if not self._regole.has_key(regola):
                raise RegolaNonTrovataError("Regola non in agenda: "+str(regola))
            regola = self._regole[regola]
            
        return self._regole.pop(regola.get_nome())
    
    
    def find_regole(self, wmemory):
        assert isinstance(wmemory, WorkingMemory)
        return [x for x in self._regole.values() if not self._penality.has_key(x.get_nome()) and x.is_valida(wmemory)]
        
        
        
class RegolaNonTrovataError(Exception):
    pass