'''
Created on 24/mar/2012

@author: Francesco Capozzo
'''
from icse.ps.wm.DictWMImpl import DictWMImpl
import os
from icse.ps.Agenda import Agenda
from icse.ps.wm.loader.DirBasedLoader import DirBasedLoader
from icse.ps.rules.Regola import Regola


def wmemory_decorator(wmemory):
    assert isinstance(wmemory, DictWMImpl)
    
    facts = wmemory.get_facts("Cella")
    
    i = 1
    j = 1
    
    try:
        print '---------'
        for j in range(1,4):
            b = "| "
            for i in range(1,4):
                b += str([(lambda t: t or " ")(x['valore']) for x in facts.values() if x['y'] == j and x['x'] == i][0]) + " "
            print b + "|"
        print '---------'
    except Exception, e:
        print
        print "Recupero dopo eccezione: "+str(e)
        print "Contenuto WORKING-MEMORY:"
        print "[" + ",\n".join([str(x) for x in facts.values()]) + "]"
    

if __name__ == '__main__':
    
    wmemory = DictWMImpl()
    agenda = Agenda()
    
    loader = DirBasedLoader(os.getcwd()+'/../games/8/')
    
    loader.load(wmemory, agenda)
    
    cicle = True
    choosed = None
    rules = []
    
    print "Regole in agenda: "+str(len(agenda._regole))
    print "Fatti caricati: "+str(len(wmemory.get_facts()))
    print "Template presenti: "+str(len(wmemory.get_templates()))
    print
    
    while cicle:
        
        if choosed != None:
            rule = rules[choosed]
            assert isinstance(rule, Regola)
            print "\t...applico: "+rule.get_nome()
            agenda.do_decrease_penalities()
            rule.attiva(wmemory, agenda)
        
        wmemory_decorator(wmemory)

        if len(agenda._penality):        
            print "Le seguenti regole sono disattivate a priori"
            for (i,t) in agenda._penality.items():
                print "\t" + str(i) + " per " + str(t) + " turni"
        
        print 
        print "Alla situazione corrente posso applicare:"
        rules = agenda.find_regole(wmemory)
        for i,r in enumerate(rules):
            print "\t"+str(i)+") "+r.get_nome()
        
        try:
            choosed = int(raw_input('Scegli la regola da applicare: '))
            print "Hai scelto: "+str(choosed)
        except ValueError:
            print "...exiting"
            cicle = False
    
    
    
    
    
    
    