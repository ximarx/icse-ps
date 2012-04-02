'''
Created on 24/mar/2012

@author: ximarx
'''
from icse.ps.wm.WorkingMemory import WorkingMemory
from icse.ps.Template import Template
from icse.ps.Fact import Fact
from icse.ps.constraints.Range import Range
from icse.ps.constraints.OrChain import OrChain
from icse.ps.constraints.NullValue import NullValue

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
        
        tplCella = Template('Cella', {
                'x' : Range(1, 3),
                'y' : Range(1, 3),
                'valore' : OrChain([Range(1,8), NullValue()])
            })
        
        wmemory.def_template(tplCella)
        
    def load_facts(self, wmemory):
        '''
        Carica la lista di fatti
        nella working memory
        @param wmemory: WorkingMemory
        '''
        for i in range(0,9):
            if i > 0: label = i 
            else: label = None
            wmemory.assert_fact(Fact(str(i+1), {
                    'x': (i / 3) + 1,
                    'y': (i % 3) + 1,
                    'valore': label
                }, 'Cella'))
        