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
from icse.ps.rules.Parser import Parser
from icse.ps.rules.grammatiche.ClipsLike import ClipsLike
import os
from icse.ps.Agenda import Agenda


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

    for v in wmemory.get_facts() :
        print "------------------------"
        print "Fatto: "+v.get_id()
        print v
        
        
    parser = Parser(ClipsLike())
    rules = parser.parse(os.getcwd()+'/../games/8/rules.txt')
    
    print "\n\n".join([str(x) for x in rules])
    
    
    agenda = Agenda(rules)
    
    print 
    print "Alla situazione corrente posso applicare:"
    for r in agenda.find_regole(wmemory):
        print "\t"+r.get_nome()
    
    
    
    
    