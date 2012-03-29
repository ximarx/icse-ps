'''
Created on 24/mar/2012

@author: ximarx
'''
from icse.ps.Fact import Fact
from icse.ps.Template import Template
from icse.ps.constraints.Range import Range
from icse.ps.constraints.OrChain import OrChain
from icse.ps.constraints.RegexMatch import RegexMatch
from icse.ps.constraints.NullValue import NullValue
from icse.ps.wm.DictWMImpl import DictWMImpl
from icse.ps.wm.loader.Naive import Naive
import json


if __name__ == '__main__':
    
    
    f1 = Fact('Cella-1', {
               'nome' : 'Cella-99',
               'x' : 1,
               'y' : 1,
               'contenuto' : 1
            }, 'Cella')
    
    f1.visitato = False

    print "Fatto: ", f1
    
    tCella = Template('Cella', {
                'x' : Range(1, 9),
                'y' : Range(1, 9),
                'contenuto' : OrChain([Range(1,9), NullValue()])
            })
    tCella.add_constraint('nome', RegexMatch('^Cella-[0-9]+$', ['i']))
    tCella.add_constraint('nome', NullValue(), 'or')
    
    print "Template: ", tCella

    tCella.validate(f1)
    
    
    wmemory = DictWMImpl()
        
    loader = Naive()
        
    loader.load_templates(wmemory)
        
    loader.load_facts(wmemory);

    for (k,v) in wmemory.get_facts().items() :
        print "####################"
        print "| Template: "+k
        for (kk,vv) in v.items():
            print "------------------------"
            print "Fatto: "+vv.get_id()
            print vv
        
        
    
    
    