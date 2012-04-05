
def serialize(wmemory):
    assert isinstance(wmemory, DictWMImpl)
    facts = wmemory.get_facts("Cella")
    b = ""
    for j in range(1,4):
        for i in range(1,4):
            b += str([(lambda t: t or "_")(x['valore']) for x in facts.values() if x['y'] == j and x['x'] == i][0])
    return b
