'''
Created on 24/mar/2012

@author: ximarx
'''
from icse.ps.wm.WorkingMemory import WorkingMemory
from icse.ps.wm.WorkingMemory import FactNotFoundError
from icse.ps.Fact import Fact
from icse.ps.Template import Template
from copy import copy

class DictWMImpl(WorkingMemory):
    '''
    Implementazione di Working Memory utilizzando una struttura
    a doppio dizionario
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.__templates = {}
        self.__facts = {}
        
        
    def assert_fact(self, fact):
        '''
        Aggiunge un nuovo fatto alla working memory
        @param fact: Fact
        '''
        if not isinstance(fact, Fact):
            raise TypeError("fact non e' un Fatto")

        templateId = fact.get_template()
        template = self.__templates[templateId]
        
        if template.validate(fact, False) : 
            self.__facts[fact.get_template()][fact.get_id()] = fact
        else:
            raise TypeError("fact non e' valido per il template")

    def retract_fact(self, fact, template = None):
        '''
        @see: WorkingMemory.retract_fact
        '''
        if isinstance(fact, Fact):
            template = fact.get_template()
            fact = fact.get_id()
        
        if not self.__facts.has_key(template) or not self.__facts[template].has_key(fact):
            raise FactNotFoundError("Il fatto non e' stato asserito")
        
        fact = copy(self.__facts[template][fact])
        del self.__facts[template][fact]
        return fact
    
    def def_template(self, template):
        '''
        @see: WorkingMemory.def_template
        '''
        if not isinstance(template, Template):
            tempKey = template
            template = Template(template)
        else:
            tempKey = template.get_templateid()
            
        if self.__facts.has_key(tempKey):
            raise TypeError("Doppia definizione di template con lo stesso id")
            
        self.__templates[tempKey] = template
        self.__facts[tempKey] = {}
    
    def get_templates(self):
        '''
        @see: WorkingMemory.get_templates
        '''
        return self.__templates
        
    def get_facts(self, template = None):
        '''
        @see: WorkingMemory.get_facts
        '''
        if template != None:
            if self.__facts.has_key(template) :
                return self.__facts[template]
            else:
                return []
    
        lfacts = []
        for facts in self.__facts.values():
            lfacts.extend(facts.values())
            
        return lfacts
    
    
if __name__ == '__main__':
    
    wm1 = DictWMImpl()
    wm1.def_template(Template("gen"))
    
    wm1.assert_fact(Fact('uno', {'v': 1}, "gen"))
    wm1.assert_fact(Fact('due', {'v': 2}, "gen"))
    wm1.assert_fact(Fact('tre', {'v': 3}, "gen"))
    
    wm2 = DictWMImpl()
    wm2.def_template(Template("gen"))
    
    wm2.assert_fact(Fact('uno', {'v': 1}, "gen"))
    wm2.assert_fact(Fact('due', {'v': 2}, "gen"))
    wm2.assert_fact(Fact('tre', {'v': 3}, "gen"))
    
    wm3 = DictWMImpl()
    wm3.def_template(Template("gen"))
    
    wm3.assert_fact(Fact('uno', {'v': 1}, "gen"))
    wm3.assert_fact(Fact('due', {'v': 2}, "gen"))
    wm3.assert_fact(Fact('tre', {'v': 3}, "gen"))
    wm3.assert_fact(Fact('qua', {'v': 4}, "gen"))

    wm4 = DictWMImpl()
    wm4.def_template(Template("gen"))
    
    wm4.assert_fact(Fact('uno', {'v': 1}, "gen"))
    wm4.assert_fact(Fact('tre', {'v': 3}, "gen"))
    wm4.assert_fact(Fact('due', {'v': 2}, "gen"))

    wm5 = DictWMImpl()
    wm5.def_template(Template("gen"))
    
    wm5.assert_fact(Fact('uno', {'v': 1}, "gen"))
    wm5.assert_fact(Fact('tre', {'v': 4}, "gen"))
    wm5.assert_fact(Fact('due', {'v': 2}, "gen"))

    
    
    print "wm1 == wm2 ? (atteso True) ", (wm1 == wm2)
    print "wm1 == wm3 ? (atteso False) ", (wm1 == wm3)
    print "wm1 == wm4 ? (atteso True) ", (wm1 == wm4)
    print "wm1 == wm5 ? (atteso False) ", (wm1 == wm5)
    