'''
Created on 30/mar/2012

@author: ximarx
'''
from icse.ps.rules.condizioni.Condizione import Condizione
from copy import copy
from icse.ps.rules.operandi.Simbolo import Simbolo

class Esiste(Condizione):
    '''
    Condizione di esistenza di una fatto, una serie di fatti
    o di uno o una serie di fatti con subcondizioni
    '''


    def __init__(self, simbolo, template, subcondizione = None ):
        '''
        Constructor
        '''
        assert isinstance(simbolo, Simbolo)
        self._simbolo = simbolo
        self._template = template
        if not isinstance(subcondizione, Condizione):
            subcondizione = None
        self._subcondizione = subcondizione  
        
    def is_valida(self, wm, simboli={}):
        facts = wm.get_facts(self._template.valuta(simboli))
        if self._subcondizione != None:
            '''
            faccio una copia dei simboli attuali, in modo
            da non alterare quelli gia esistenti
            visto che ho bisogno di inserire 
            il nuovo simbolo subito per valutare il resto dell'espressione
            '''
            for fact in facts.values():
                in_simboli = copy(simboli)
                # aggiungo il simbolo al dizionario temporaneo
                in_simboli[str(self._simbolo)] = fact
                # valuto l'espressione
                if self._subcondizione.is_valida(wm, in_simboli):
                    # condizione verificata per SIMBOLO = fact
                    # eseguo una merge fra i simboli
                    simboli.update(in_simboli)
                    return True
        else:
            ''' 
            controllo la lunghezza dei fatti trovati
            e verifico se quindi la condizione di esistenza
            e' vera (e se per caso ho trovato un solo elemento)
            '''
            if len(facts) == 1:
                return True
            else:
                '''
                Ho trovato nessuno o piu di un fatto
                con quelle caratteristiche
                '''
                return False
        
        
    def __str__(self):
        '''
        Rappresentazione della regola in linguaggio naturale
        nella forma (se la subcondizione sia speficiata):
            "esiste un solo $SIMBOLO di tipo Template tale che Subcondizione sia vero"
        o nella forma (se la subcondizione non e' specificata):
            "esiste un solo $SIMBOLO di tipo Template
        '''
        stringa = [
                'esiste un',
                str(self._simbolo),
                'di tipo',
                str(self._template)
            ]
        if self._subcondizione:
            stringa.append('tale che')
            stringa.append(str(self._subcondizione))
        return " ".join(stringa)
        
         
        