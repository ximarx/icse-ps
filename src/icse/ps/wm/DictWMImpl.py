'''
Created on 24/mar/2012

@author: ximarx
'''
from icse.ps.wm.WorkingMemory import WorkingMemory
from icse.ps.wm.WorkingMemory import FactNotFoundError
from icse.ps.Fact import Fact
from icse.ps.Template import Template

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
        
        if template.is_valid(fact) : 
            self.__facts[fact.get_template()] = fact
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
        
        return self.__facts[template].pop(fact)
    
    def def_template(self, template):
        '''
        @see: WorkingMemory.def_template
        '''
        if not isinstance(template, Template):
            tempKey = template
            template = Template(template)
        else:
            tempKey = template.get_id()
            
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
        if template != None and self.__facts.has_key(template) :
            return {template : self.__facts[template]}
    
        self.__facts
    
    