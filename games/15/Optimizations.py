from icse.ps.wm.DictWMImpl import DictWMImpl
import traceback
import sys

def serializer(wmemory):
    assert isinstance(wmemory, DictWMImpl)
    facts = wmemory.get_facts("Cella")
    b = ""
    
    matrix = [[" " for _ in range(0,4)] for _ in range(0,4)]
    for fact in facts.values():
        if fact['valore'] == None:
            matrix[int(fact['y'])-1][int(fact['x'])-1] = "_"
        else:
            matrix[int(fact['y'])-1][int(fact['x'])-1] = str(fact['valore'])

    b = ";".join([",".join(y) for y in matrix])
    
    return b

def decorator(wmemory):
    assert isinstance(wmemory, DictWMImpl)
    
    facts = wmemory.get_facts("Cella")

    matrix = [[" " for _ in range(0,4)] for _ in range(0,4)]
    
    try:
        
        for fact in facts.values():
            if fact['valore'] == None:
                matrix[int(fact['y'])-1][int(fact['x'])-1] = " #"
            else:
                matrix[int(fact['y'])-1][int(fact['x'])-1] = str(fact['valore']).ljust(2, " ")
        
        buf = "----------------\n"
        buf += "| " + " |\n| ".join([" ".join(y) for y in matrix]) + " |\n"
        buf += "-----------------\n"
        
        print buf
        
    except Exception, e:
        traceback.print_exc(file=sys.stdout)
        print "Contenuto WORKING-MEMORY:"
        if isinstance(facts, dict): 
            print "[" + ",\n".join([str(x) for x in facts.values()]) + "]"
        else:
            print "[" + ",\n".join([str(x) for x in facts]) + "]"
    