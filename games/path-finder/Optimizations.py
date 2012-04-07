from icse.ps.wm.DictWMImpl import DictWMImpl

def serializer(wmemory):
    assert isinstance(wmemory, DictWMImpl)
    pedone = wmemory.get_facts("Pedone")["Pedone"]
    return ",".join([str(pedone["y"]), str(pedone["x"])])

def decorator(wmemory):
    assert isinstance(wmemory, DictWMImpl)
    
    try:
    
        matrix = [["." for _ in range(0,21)] for _ in range(0,21)]
        
        goal = wmemory.get_facts("Goal")["Goal"]
        matrix[int(goal['y']) - 1][int(goal['x']) - 1] = "@"
        
        pedone = wmemory.get_facts("Pedone")["Pedone"]
        matrix[int(pedone['y']) - 1][int(pedone['x']) - 1] = "$"
        
        walls = wmemory.get_facts("Muro")
        for wall in walls.values():
            matrix[int(wall['y']) - 1][int(wall['x']) - 1] = "#"
    
        buf = "\n".join(["".join(y) for y in matrix])
        
        print buf
        
    except Exception:
        wmemory_decorator(wmemory)
    