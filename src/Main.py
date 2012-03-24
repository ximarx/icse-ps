'''
Created on 24/mar/2012

@author: ximarx
'''
from icse.ps.Fact import Fact
from icse.ps.wm.loader.Naive import Naive
from icse.ps.wm.DictWMImpl import DictWMImpl

if __name__ == '__main__':
    
    
    f1 = Fact('Cella-1', {
               'nome' : 'Cella',
               'x' : '1',
               'y' : '1',
               'contenuto' : 1
            }, 'Cella')
    
    f1.visitato = False

    print "Fatto: ", f1
    print "Attributi (solo chiavi): ", f1.get_attributes().keys()
    print "Attributi (completi): ", f1.get_attributes()
    
    wmemory = DictWMImpl()
    
    loader = Naive()
    
    loader.load_templates(wmemory)
    
    loader.load_facts(wmemory);
    