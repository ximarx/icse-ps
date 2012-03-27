'''
Created on 27/mar/2012

@author: ximarx
'''

def new_object_from_complete_classname(qclass, constrParams = []):
    
    lastdot = qclass.rfind('.')
    modulename = qclass[0:lastdot]
    classname = qclass[lastdot+1:]
    
    return new_object_from_classname(classname, constrParams, modulename)
    
    #__import__('icse.ps.constraints.OrChain')
    #chain2 = globals()['OrChain']()
    
def new_object_from_classname(classname, constrParams = [], modulename = None):
    if modulename != None:
        imported = __import__(modulename,  globals(), locals(), [classname], -1)
        attr = getattr(imported, classname)
        return attr(*constrParams)
    else:
        return globals()[classname](*constrParams)

    