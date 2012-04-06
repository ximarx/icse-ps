'''
Created on 05/apr/2012

@author: Francesco Capozzo
'''
from icse.ps.algoritmi.Algoritmo import Algoritmo
from icse.ps.algoritmi.RisultatoAlgoritmo import RisultatoAlgoritmo
import sys
from icse.ps.rules.Regola import Regola
from copy import deepcopy

class Astar(Algoritmo):
    '''
    Algoritmo A*
    
    Da wikipedia: http://en.wikipedia.org/wiki/A*_search_algorithm
    function A*(start,goal)
         closedset := the empty set    // The set of nodes already evaluated.
         openset := {start}    // The set of tentative nodes to be evaluated, initially containing the start node
         came_from := the empty map    // The map of navigated nodes.
     
         g_score[start] := 0    // Cost from start along best known path.
         h_score[start] := heuristic_cost_estimate(start, goal)
         f_score[start] := g_score[start] + h_score[start]    // Estimated total cost from start to goal through y.
     
         while openset is not empty
             current := the node in openset having the lowest f_score[] value
             if current = goal
                 return reconstruct_path(came_from, came_from[goal])
     
             remove current from openset
             add current to closedset
             for each neighbor in neighbor_nodes(current)
                 if neighbor in closedset
                     continue
                 tentative_g_score := g_score[current] + dist_between(current,neighbor)
     
                 if neighbor not in openset
                     add neighbor to openset
                     h_score[neighbor] := heuristic_cost_estimate(neighbor, goal)
                     tentative_is_better := true
                 else if tentative_g_score < g_score[neighbor]
                     tentative_is_better := true
                 else
                     tentative_is_better := false
     
                 if tentative_is_better = true
                     came_from[neighbor] := current
                     g_score[neighbor] := tentative_g_score
                     f_score[neighbor] := g_score[neighbor] + h_score[neighbor]
     
         return failure
     
     function reconstruct_path(came_from, current_node)
         if came_from[current_node] is set
             p := reconstruct_path(came_from, came_from[current_node])
             return (p + current_node)
         else
             return current_node    
    
    
    '''

    def __init__(self, wmemory, agenda):
        '''
        Inizializza l'algoritmo (delega al super costruttore)
        '''
        Algoritmo.__init__(self, wmemory, agenda)
        
        
    def execute(self, goal):
        self._prepare_lamda(goal)
        
        closed_set = []
        open_set = []
        came_from = {}
        
        g_scores = {}
        h_scores = {}
        f_scores = {}
        
        # se non e' fra le opzioni, uso una funzione a valore costante
        # in modo da rendere la A* come una breadth non informata
        heuristic_cost_estimate = self._get_option('h_lambda', (lambda t:0))
        assert callable(heuristic_cost_estimate),\
            "Funzione h_lambda non valida: "+str(type(heuristic_cost_estimate))
            
        dist_between = self._get_option("distance_lambda", (lambda s1,s2,regola:1))
        assert callable(dist_between),\
            "Funzione distance_lambda non valida"
        
        h_factor = int(self._get_option("h_factor", 1))
        
        g_scores[self._wmemory] = 0
        h_scores[self._wmemory] = heuristic_cost_estimate(self._wmemory)
        f_scores[self._wmemory] = g_scores[self._wmemory] + (h_factor * h_scores[self._wmemory])
        
        open_set.append(self._wmemory)
        
        while len(open_set) > 0:
            # prendo il nodo in open_set con il minor valore f_scores
            stato = self._get_max_fscores(open_set, f_scores)
            
            if self._is_goal(stato):
                # ho trovato il goal, preparo e restituisco RisultatoAlgoritmo
                return RisultatoAlgoritmo(stato, self._reconstuct_path(stato, came_from), True)
            
            open_set.remove(stato)
            closed_set.append(stato)
            
            #agenda = self._agenda
            #assert isinstance(agenda, Agenda)
            
            rules = self._agenda.find_regole(stato)
            
            for rule in rules:
                assert isinstance(rule, Regola)
                
                #creo una copia dello stato attuale
                copiastato = deepcopy(stato)
                
                # rivaluto la regola il nuovo copiastato
                # in modo da risolvere nuovamente
                # le variabili nella regola
                rule.is_valida(copiastato)
                
                rule.attiva(copiastato, self._agenda)
                
                if closed_set.count(copiastato) != 0:
                    continue
            
                tentative_g_score = g_scores[stato] + dist_between(stato, copiastato, rule)
                if open_set.count(copiastato) == 0 :
                    # prima volta che giungo in questo stato
                    open_set.append(copiastato)
                    h_scores[copiastato] = heuristic_cost_estimate(copiastato)
                    tentative_is_better = True
                elif tentative_g_score < g_scores[copiastato]:
                    # sono gia stato qui, ma questo percorso e' migliore
                    # del precedente
                    
                    tentative_is_better = True
                else:
                    tentative_is_better = False
                    
                if tentative_is_better :
                    # devo aggiornare lo stato perche questo stato
                    # e' nuovo o migliore del precedente path
                    came_from[copiastato] = (stato, rule.get_nome())
                    g_scores[copiastato] = tentative_g_score
                    f_scores[copiastato] = tentative_g_score + (h_factor * h_scores[copiastato])
                    
        if stato :
            return RisultatoAlgoritmo(stato, self._reconstuct_path(stato, came_from), False)
        else :
            return RisultatoAlgoritmo(self._wmemory, None, False)
        
        
    def _get_max_fscores(self, openset, fscores):
        assert isinstance(openset, list)
        assert isinstance(fscores, dict)
        
        current_min = (None, sys.maxint)
        
        for state in openset:
            score = fscores[state]
            if score < current_min[1]:
                current_min = (state, score)
                
        return current_min[0]
    
    def _reconstuct_path(self, stato, came_from):
        assert isinstance(came_from, dict)
        if came_from.has_key(stato):
            popped = came_from.pop(stato)
            p = self._reconstuct_path(popped[0], came_from)
            p.extend([popped[1]])
            return p
        else:
            return []
            