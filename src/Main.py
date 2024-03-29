'''
Created on 24/mar/2012

@author: Francesco Capozzo
'''
from icse.ps.wm.DictWMImpl import DictWMImpl
import os
from icse.ps.Agenda import Agenda
from icse.ps.wm.loader.DirBasedLoader import DirBasedLoader
from icse.ps.rules.Regola import Regola
import time
from icse.ps.wm.loader.PackageLoader import PackageLoader
from genericpath import isdir, isfile
import sys
import traceback


def wmemory_decorator(wmemory):
    assert isinstance(wmemory, DictWMImpl)
    facts = wmemory.get_facts()
    print "[" + ",\n".join([str(x) for x in facts]) + "]"

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
            try:
                rule = rules[choosed]
                assert isinstance(rule, Regola)
                print "\t...applico: "+rule.get_nome()
                agenda.do_decrease_penalities()
                rule.attiva(wmemory, agenda)
            except Exception, e:
                print "Qualcosa e' andato storto nell'applicatione: "+str(e)
        
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
        
    

def main_loop():
    
    GAMES_DIR = os.getcwd()+'/../games/'
    
    print "GAMES_DIR: ", GAMES_DIR
    print 
    
    games = [x for x in os.listdir(GAMES_DIR) if isdir(GAMES_DIR + "/" + x) and isfile(GAMES_DIR+"/"+x+"/"+"package.json")]
    
    if len(games) < 1:
        print "Non ho trovato nessun gioco. Ciao ciao...."
        return False

    while True:
    
        print "Questi sono i giochi che ho trovato:"
        for i, game in enumerate(games):
            print "\t"+str(i)+") "+str(game)
            
        print "\t.) Qualsiasi altra selezione per uscire"
        
        try:
            choosed = int(raw_input('Cosa vuoi che risolva? '))
            print "Hai scelto: "+str(games[choosed])
            print
            print "--------------------------------"
            try:
                solve_game(GAMES_DIR+"/"+games[choosed]+"/")
            except Exception:
                traceback.print_exc(file=sys.stdout)
            print "--------------------------------"
            print
            
        except ValueError:
            print "...Ciao Ciao..."
            return True
    
def solve_game(gamepath):    
    
    wmemory = DictWMImpl()
    agenda = Agenda()
    goals = []
    algs = []
    optimizations = {
        'status-decorator' : lambda t: wmemory_decorator(t),
        'status-serializer' : lambda t: t
    }
    
    loader = PackageLoader(gamepath)
    
    loader.load(wmemory, agenda, goals, algs, optimizations)

    optimizations['status-decorator'](wmemory)

    for (name, alg, note) in algs:     
        start = time.time()
        print "Inizio "+name+" ("+note+") :\n\t", time.strftime("%d %b %Y %H:%M:%S +0000", time.gmtime())
        result = alg.execute(goals[0])
        print "Fine:\n\t", time.strftime("%d %b %Y %H:%M:%S +0000", time.gmtime()) 
        print "Durata: circa " + str(int(time.time() - start)) + " secondi (+/- 1 secondo)"
        print result
        optimizations['status-decorator'](result.get_result())
        print "-------------------"
        print
        

    

if __name__ == '__main__':
    
    main_loop()
    