
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
            4: (1,4),
            5: (2,1),
            6: (2,2),
            7: (2,3),
            8: (2,4),
            9: (3,1),
            10: (3,2),
            11: (3,3),
            12: (3,4),
            13:  (4,1),
            14:  (4,2),
            15:  (4,3),            
            None: (4,4)
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
            4: (1,4),
            5: (2,1),
            6: (2,2),
            7: (2,3),
            8: (2,4),
            9: (3,1),
            10: (3,2),
            11: (3,3),
            12: (3,4),
            13:  (4,1),
            14:  (4,2),
            15:  (4,3),            
            None: (4,4)
        }

    sommatoria = 0
    celle = wmemory.get_facts("Cella")
    for cella in celle.values():
        y,x = posizioni[cella['valore']]
        d = abs( cella['x'] - x) + abs( cella['y'] - y )
        sommatoria += d
        
        
    return sommatoria