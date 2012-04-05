'''
Created on 05/apr/2012

@author: Francesco Capozzo
'''
from icse.ps.wm.WorkingMemory import WorkingMemory

class RisultatoAlgoritmo(object):
    '''
    Rappresenta uno stato risultato di un Algoritmo
    ottenuto tramite Algoritmo.execute(goal)
    '''

    def __init__(self, endstate, path = None, success = True):
        '''
        Costruisce l'oggetto
        @param endstate: WorkingMemory la workingmemory nello stato terminale
            dell'esecuzione. Puo' rappresentare la soluzione (se success e' vero)
            oppure l'ultimo stato tenticativo se l'algoritmo non ha avuto successo
        @param path: [Regole] una lista di regole da applicare in successione allo stato
            iniziale per giungere allo stato finale individuato dall'algoritmo
        @param success: bool indica se l'algoritmo e' terminato con successo (e quindi
            la condizione di goal e' esaudita) oppure se l'algoritmo e' terminato
            con insuccesso (se si sono raggiunti dei vincoli di esecuzione massima
            oppure se semplicemente dopo una ricerca esaustiva nello spazio delle soluzioni
            non e' stata individuata alcuna soluzione valida)
            Nel caso success sia False, il valore di get_result rappresenta l'ultimo stato
            tentato o lo stato iniziale, mentre get_path rappresenta il path verso lo stato
            get_result (o [] se get_result = inizio)
        '''
        assert isinstance(endstate, WorkingMemory)
        if path == None:
            path = []
        
        self._endstate = endstate
        self._path = path
        self._success = success
        
    def get_path(self):
        '''
        Restituisce la lista di regole da applicare in sequenza
        per ottenere lo stato indicato da get_result
        partendo dallo stato iniziale
        @return: [Regola.get_nome()]
        '''
        return self._path
    
    def get_result(self):
        '''
        Restituisce lo stato di terminazione dell'algoritmo
        Rappresenta una soluzione valida al problema
        SE is_success = True, altrimenti rappresenta
        l'ultimo stato testato prima della condizione di terminazione
        oppure lo stato iniziale
        @return WorkingMemory
        '''
        return self._endstate
    
    def is_success(self):
        '''
        Indica lo stato di terminazione dell'algoritmo
        che ha generato questo oggetto
        @return bool
        '''
        return self._success
    
    
    def __str__(self):
        return "\n".join([
                " ".join([
                    "Algoritmo terminato con stato",
                    str(self._success)
                ]),
                "\tPath:\n\t\t"+"\n\t\t".join(self.get_path()),
            ])
    