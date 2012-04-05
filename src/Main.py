'''
Created on 24/mar/2012

@author: Francesco Capozzo
'''
from icse.ps.wm.DictWMImpl import DictWMImpl
import os
from icse.ps.Agenda import Agenda
from icse.ps.wm.loader.DirBasedLoader import DirBasedLoader
from icse.ps.rules.Regola import Regola
from copy import deepcopy
import random
import time
from icse.ps.algoritmi.Astar import Astar
import sys


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
        print "Stato errato, recupero eccezione: "+str(e)
        print "Contenuto WORKING-MEMORY:"
        print "[" + ",\n".join([str(x) for x in facts.values()]) + "]"
    
    
def is_goal(wmemory):
    return (serialize(wmemory) == "1238_4765")

def serialize(wmemory):
    assert isinstance(wmemory, DictWMImpl)
    facts = wmemory.get_facts("Cella")
    b = ""
    for j in range(1,4):
        for i in range(1,4):
            b += str([(lambda t: t or "_")(x['valore']) for x in facts.values() if x['y'] == j and x['x'] == i][0])
    return b

def manhattan_distance(wmemory):
    '''
    Calcola la distanza di ogni casella dalla sua posizione naturale
    '''
    posizioni = {
            1: (1,1),
            2: (1,2),
            3: (1,3),
            4: (2,3),
            5: (3,3),
            6: (3,2),
            7: (3,1),
            8: (2,1),
            None: (2,2)
        }

    sommatoria = 0
    celle = wmemory.get_facts("Cella")
    for cella in celle.values():
        y,x = posizioni[cella['valore']]
        d = abs( cella['x'] - x) + abs( cella['y'] - y )
        sommatoria += d
        
        
    return sommatoria
    
def tasselli_fuoriposto(wmemory):
    '''
    Calcola il numero di tasselli fuoriposto
    '''
    
    posizioni = {
            1: (1,1),
            2: (1,2),
            3: (1,3),
            4: (2,3),
            5: (3,3),
            6: (3,2),
            7: (3,1),
            8: (2,1),
            None: (2,2)
        }
    
    celle = wmemory.get_facts("Cella")
    errate = 0
    for cella in celle.values():
        y,x = posizioni[cella['valore']]
        if cella['x'] != x or cella['y'] != y:
            errate += 1
    
    return errate
    

def _gioca():
    
    wmemory = DictWMImpl()
    agenda = Agenda()
    goals = []
    
    loader = DirBasedLoader(os.getcwd()+'/../games/8/')
    
    loader.load(wmemory, agenda, goals)
    
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
        
    

if __name__ == '__main__':
    
    wmemory = DictWMImpl()
    agenda = Agenda()
    goals = []
    
    loader = DirBasedLoader(os.getcwd()+'/../games/8-harder/')
    
    loader.load(wmemory, agenda, goals)

    wmemory_decorator(wmemory)

    ablind = Astar(wmemory, agenda)
    atasselli = Astar(wmemory, agenda)
    atasselli.set_options({
            'h_lambda' : tasselli_fuoriposto
        })
    amanhattan = Astar(wmemory, agenda)
    amanhattan.set_options({
            'h_lambda' : manhattan_distance
        })
    amanhattan_f2 = Astar(wmemory, agenda)
    amanhattan_f2.set_options({
            'h_lambda' : manhattan_distance,
            'h_factor' : 2
        })
    
    algs = [("A* tasselli", atasselli), ("A* manhattan", amanhattan), ("A* manhattan (fattore h * 2)", amanhattan_f2), ("A* cieca", ablind)]

    for (name, alg) in algs:     
        start = time.time()
        print "Inizio "+name+":\n\t", time.strftime("%d %b %Y %H:%M:%S +0000", time.gmtime())
        result = alg.execute(goals[0])
        print "Fine:\n\t", time.strftime("%d %b %Y %H:%M:%S +0000", time.gmtime()) 
        print "Durata: circa " + str(int(time.time() - start)) + " secondi (+/- 1 secondo)"
        print result
        print "-------------------"
        print
        
    
    '''
    
    generati = {
            serialize(wmemory) : None
        }
    i = 0
    L = [(wmemory, agenda)]
    
    
    while len(L) > 0:
        primo_stato = L[0][0]
        primo_agenda = L[0][1]
        i += 1
        if i == 1000:
            i = 0
            print "Mille cicli... in " + str(int(time.time() - start)) + " secondi"
            print "\tDimensione di L: "+str(len(L))
            print "\tDimensione di Generati: "+str(len(generati))
            print "\tSto per analizzare:"
            wmemory_decorator(primo_stato)
            #raw_input('...premi per continuare...')
            
        if is_goal(primo_stato):
            print "Goal raggiunto!!!"
            print "...ma in " + str(int(time.time() - start)) + " secondi"
            wmemory_decorator(primo_stato)
            break
        else:
            L = L[1:]
            rules = primo_agenda.find_regole(primo_stato)
            primo_agenda.do_decrease_penalities()
            primo_serializzato = serialize(primo_stato)
            random.shuffle(rules)
            #print "Generati ------"
            for rule in rules:
                assert isinstance(rule, Regola)
                cagenda = deepcopy(primo_agenda)
                cwm = deepcopy(primo_stato)
                rule.is_valida(cwm)
                rule.attiva(cwm, cagenda)
                s = serialize(cwm)
                #evita di ripercorrere strade gia percorse
                if not generati.has_key(s):
                    generati[s] = primo_serializzato
                    #print rule.get_nome()
                    #wmemory_decorator(cwm)
                    L.insert(0, (cwm, cagenda))
                    
            #raw_input('...premi per continuare...')
    
    '''



    
    
    
    
    
    