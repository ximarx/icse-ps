'''
Created on 24/mar/2012

@author: ximarx
'''
from icse.ps.wm.DictWMImpl import DictWMImpl
import os
from icse.ps.Agenda import Agenda
from icse.ps.wm.loader.DirBasedLoader import DirBasedLoader


if __name__ == '__main__':
    
    wmemory = DictWMImpl()
    agenda = Agenda()
    
    loader = DirBasedLoader(os.getcwd()+'/../games/8/')
    
    loader.load(wmemory, agenda)
    
    print 
    print "Alla situazione corrente posso applicare:"
    for r in agenda.find_regole(wmemory):
        print "\t"+r.get_nome()
    
    
    
    
    
    