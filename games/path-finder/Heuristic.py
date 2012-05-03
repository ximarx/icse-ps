
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

def EuclideaDistance(oldmemory, newmemory, rule):
    '''
    Calcola la distanza percorsa dal pedone
    durante il passo come distanza euclidea
    '''
    
    from icse.ps.wm.WorkingMemory import WorkingMemory
    from icse.ps.rules.Regola import Regola
    
    assert isinstance(oldmemory, WorkingMemory)
    assert isinstance(newmemory, WorkingMemory)
    assert isinstance(rule, Regola)
    
    pedone_old = oldmemory.get_facts("Pedone")["Pedone"]
    pedone_new = newmemory.get_facts("Pedone")["Pedone"]
    
    d = pow( pow( pedone_old['x'] - pedone_new['x'], 2) + pow( pedone_old['y'] - pedone_new['y'], 2) , (1./2))
    
    return d