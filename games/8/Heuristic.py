
def TasselliFuoriPosto(wmemory):
    '''
    Calcola il numero di tasselli fuoriposto
    '''
    
    from icse.ps.wm.WorkingMemory import WorkingMemory
    
    assert isinstance(wmemory, WorkingMemory)
    
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


def ManhattanDistance(wmemory):
    '''
    Calcola la distanza di ogni casella dalla sua posizione naturale
    '''
    
    from icse.ps.wm.WorkingMemory import WorkingMemory
    
    assert isinstance(wmemory, WorkingMemory)
    
    
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