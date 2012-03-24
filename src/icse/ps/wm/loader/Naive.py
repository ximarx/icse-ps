'''
Created on 24/mar/2012

@author: ximarx
'''
from icse.ps.wm.WorkingMemory import WorkingMemory
from icse.ps.Template import Template
from icse.ps.Fact import Fact

class Naive:
    '''
    Loader di fatti
    Semplicemente crea le classi e le inserisce in working memory
    usando il codice hard-coded
    '''

    def __init__(self):
        '''
        Constructor
        '''
        
    def load_templates(self, wmemory):
        '''
        Carica la lista dei template
        nella working memory
        @param wmemory: WorkingMemory 
        '''
        if not isinstance(wmemory, WorkingMemory) :
            raise TypeError("wmemory non e' una WorkingMemory")
        
        t = Template('numero')
        t.append_attribute(Template.Attribute('valore', True, Template.Attribute.TYPE_INT))
        
        wmemory.def_template(t)
        
    def load_facts(self, wmemory):
        '''
        Carica la lista di fatti
        nella working memory
        @param wmemory: WorkingMemory
        '''
        wmemory.assert_fact(Fact('1', {'valore': 1}, 'numero'))
        