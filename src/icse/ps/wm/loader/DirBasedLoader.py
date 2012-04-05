'''
Created on 02/apr/2012

@author: Francesco Capozzo
'''
from genericpath import exists
from icse.ps.rules.Parser import Parser as RuleParser
from icse.ps.facts.templates.Parser import Parser as TemplateParser
from icse.ps.facts.Parser import Parser as FactParser
from icse.ps.wm.WorkingMemory import WorkingMemory
from icse.ps.Agenda import Agenda
from icse.ps.rules.grammatiche.ClipsLike import ClipsLike
from icse.ps.rules.goal.ClipsLike import ClipsLike as GoalClipsLike


class DirBasedLoader(object):
    '''
    Carica fatti, template e regole [e magari anche funzioni]
    da una directory
    Il loader richiede che:
        - /DIR/rules.txt : sia il file che contiene le regole interpretabili da ClipsLike parser
        - /DIR/templates.json : sia il file che contiene i template interpretatibili tramite icse.ps.facts.templates.Parser.Parser
        - /DIR/facts.json : sia il file che contiene i fatti interpretabili tramite icse.ps.facts.Parser.Parser
        - /DIR/goals.txt : sia il file che contiene la definizione dei goal interpretabili tramite icse.ps.goal.ClipsLike
        
    '''


    def __init__(self, dirpath):
        '''
        Constructor
        '''
        assert isinstance(dirpath, str),\
            "Atteso dirpath di tipo string, fornito "+str(type(dirpath))
            
        if not exists(dirpath):
            raise TypeError("Percorso non valido")
            
        self._dirpath = dirpath
            
            
    def load(self, wmemory, agenda, goals):
        
        assert isinstance(wmemory, WorkingMemory)
        assert isinstance(agenda, Agenda)
        assert isinstance(goals, list)
                
        tparser = TemplateParser()
        
        [wmemory.def_template(x) for x in tparser.load_file(self._dirpath+'/templates.json')] 
    
        fparser = FactParser()
    
        [wmemory.assert_fact(x) for x in fparser.load_file(self._dirpath + "/facts.json")]
        
        rparser = RuleParser(ClipsLike())

        [agenda.set_regola(x) for x in rparser.parse(self._dirpath + "/rules.txt")]
        
        gparser = RuleParser(GoalClipsLike())
        
        goals.extend(gparser.parse(self._dirpath + "/goals.txt"))
        
        
        