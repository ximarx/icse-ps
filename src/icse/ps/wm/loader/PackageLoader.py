'''
Created on 02/apr/2012

@author: Francesco Capozzo
'''
from genericpath import exists, isfile
from icse.ps.wm.WorkingMemory import WorkingMemory
from icse.ps.Agenda import Agenda
import json
from icse.ps import Utils
from icse.ps.algoritmi.Algoritmo import Algoritmo
import sys


class PackageLoader(object):
    '''
    Carica fatti, template e regole [e magari anche funzioni]
    da una directory
    Il loader richiede che:
        - /DIR/rules.txt : sia il file che contiene le regole interpretabili da ClipsLike parser
        - /DIR/templates.json : sia il file che contiene i template interpretatibili tramite icse.ps.facts.templates.Parser.Parser
        - /DIR/facts.json : sia il file che contiene i fatti interpretabili tramite icse.ps.facts.Parser.Parser
        - /DIR/goals.txt : sia il file che contiene la definizione dei goal interpretabili tramite icse.ps.goal.ClipsLike
        
    '''


    def __init__(self, dirpath):
        '''
        Constructor
        '''
        assert isinstance(dirpath, str),\
            "Atteso dirpath di tipo string, fornito "+str(type(dirpath))
            
        if not exists(dirpath):
            raise TypeError("Percorso non valido")
            
        self._dirpath = dirpath
        self._manifest = None
            
    
    def manifest(self):
        '''
        Legge il manifesto del problema pacchettizzato
        e restituisce le informazioni dict
        '''
        if self._manifest == None:
            if isfile(self._dirpath):
                '''Decomprimo il package in una directory temporanea'''
                raise NotImplementedError("Lettura da package zippato non implementata ancora")
        
            manifest_file = self._dirpath.rstrip("/")+"/package.json"
            
            self._manifest = json.load(open(manifest_file))
        
        return self._manifest
    
    def get_manifest_property(self, prop):
        '''
        Restituisce il valore di una proprieta all'interno del manifest
        '''
        assert isinstance(prop, str)
        
    
            
    def load(self, wmemory, agenda, goals, algs, optimizations):
        
        assert isinstance(wmemory, WorkingMemory)
        assert isinstance(agenda, Agenda)
        assert isinstance(goals, list)
        assert isinstance(algs, list)
        
        m = self.manifest()
        
        tparser_class = m['templates']['parser']
        tparser_file = m['templates']['file']
        tparser = Utils.new_object_from_complete_classname(tparser_class)
        [wmemory.def_template(x) for x in tparser.load_file(self._dirpath.rstrip("/")+'/'+tparser_file)] 
    
        fparser_class = m['initial-facts']['parser']
        fparser_file = m['initial-facts']['file']
        fparser = Utils.new_object_from_complete_classname(fparser_class)
        [wmemory.assert_fact(x) for x in fparser.load_file(self._dirpath.rstrip("/")+'/'+fparser_file)]
        
        rparser_class = m['rules']['parser']
        rgrammar_class = m['rules']['grammar']
        rules_file = m['rules']['file']
        rparser = Utils.new_object_from_complete_classname(rparser_class, [
                        Utils.new_object_from_complete_classname(rgrammar_class)
                    ])
        [agenda.set_regola(x) for x in rparser.parse(self._dirpath.rstrip("/")+'/'+rules_file)]


        gparser_class = m['goals']['parser']
        ggrammar_class = m['goals']['grammar']
        goals_file = m['goals']['file']
        gparser = Utils.new_object_from_complete_classname(gparser_class, [
                        Utils.new_object_from_complete_classname(ggrammar_class)
                    ])
        
        goals.extend(gparser.parse(self._dirpath.rstrip("/") + "/" + goals_file))
        
        strategies = m["env"]["strategies"]
        assert isinstance(strategies, list) and len(strategies) > 0
        for strategy in strategies:
            try:
                alg_class = strategy['class']
                alg_options = strategy['options']
                alg_name = strategy['name']
                alg_note = strategy['note']
                
                alg_obj = Utils.new_object_from_complete_classname(alg_class, [wmemory, agenda])
                
                
                '''
                Leggo i tipi dei valori delle opzioni,
                interpreto i tipi stringa come riferimenti a nomi di funzioni
                '''
                assert isinstance(alg_options, dict)
                for (k,v) in alg_options.items():
                    if isinstance(v, basestring):
                        funcname = v[v.rfind('.') + 1:]
                        modulo = Utils.import_path(self._dirpath.rstrip("/") + "/" + v )
                        alg_options[k] = getattr(modulo, funcname)
                        
                assert isinstance(alg_obj, Algoritmo)
                alg_obj.set_options(alg_options)
                algs.append((alg_name, alg_obj, alg_note))
            except Exception, e:
                print >> sys.stderr, "Errore durante intepretazione di una strategia (verra' ignorata): "+str(e)
        
        _optimizations = m["optimizations"]
        if isinstance(_optimizations, dict):
            for (k,v) in _optimizations.items():
                if isinstance(v, basestring):
                    funcname = v[v.rfind('.') + 1:]
                    modulo = Utils.import_path(self._dirpath.rstrip("/") + "/" + v )
                    optimizations[k] = getattr(modulo, funcname)
            
        for (_,alg,_) in algs:
            alg.set_optimizations(optimizations)
        
        