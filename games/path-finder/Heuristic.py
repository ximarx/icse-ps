
def ManhattanDistance(wmemory):
    '''
    Calcola la distanza fra il pedone e il goal
    in termini di somma fra la differenze delle coordinate
    '''
    
    from icse.ps.wm.WorkingMemory import WorkingMemory
    
    assert isinstance(wmemory, WorkingMemory)
    
    pedone = wmemory.get_facts("Pedone")["Pedone"]
    goal = wmemory.get_facts("Goal")["Goal"]

    d = abs( pedone['x'] - goal['x']) + abs( pedone['y'] - goal['y'] )
        
    return d