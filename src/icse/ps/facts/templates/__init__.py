from icse.ps.Utils import new_object_from_complete_classname
from copy import copy


__all__ = [ 'constraints', 'chains', 'factory', 'TipoCondizioneTemplateNonValidaError' ]

_constraints = {
        'NullValue': 'icse.ps.constraints.NullValue.NullValue',
        'Range': 'icse.ps.constraints.Range.Range',
        'RegexMatch': 'icse.ps.constraints.RegexMatch.RegexMatch',
        'Set': 'icse.ps.constraints.ValuesSet.ValuesSet',
        'Boolean': 'icse.ps.constraints.BooleanSet.BooleanSet'
    }

_chains = {
        'Or': 'icse.ps.constraints.OrChain.OrChain',
        'And': 'icse.ps.constraints.AndChain.AndChain',
        'Not': 'icse.ps.constraints.Not.Not',
        'Xor': 'icse.ps.constraints.XorChain.XorChain'
    }

def constraints():
    return  _constraints.keys()

def chains():
    return _chains.keys()

def factory(nome, args = None):
    if args == None:
            args = []

    merged = copy(_chains)
    merged.update(_constraints)
    
    if not merged.has_key(nome):
        raise TipoCondizioneTemplateNonValidaError("Condizione sconosciuta su template: "+str(nome))
    
    classe = merged[nome]
    
    if classe.startswith("."):
        classe = classe[1:]
        classe = ".".join(["icse.ps.facts.templates",
                           classe,
                           classe])
        
    return new_object_from_complete_classname(classe, args)
    

class TipoCondizioneTemplateNonValidaError(Exception):
    pass