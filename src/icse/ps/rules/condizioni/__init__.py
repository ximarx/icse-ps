from icse.ps.rules.condizioni.Uguale import Uguale
from icse.ps.rules.operandi.Null import Null
from icse.ps.Utils import new_object_from_complete_classname
from copy import copy

__all__ = [ 'condizioni', 'congiunzioni', 'factory', 'CondizioneNonValidaError' ]

_condizioni = {
        'esiste': '.Esiste',
        'uguale': '.Uguale',
        'maggiore': '.Maggiore',
        'minore': '.Minore'
    }

_congiunzioni = {
        'not': '.Not',
        'and': '.And',
        'xor': '.Xor',
        'or': '.Or',
    }

def condizioni():
    return  _condizioni.keys()

def congiunzioni():
    return  _congiunzioni.keys()

def factory(nome, args = None):
    if args == None:
        args = []
    merged = copy(_congiunzioni)
    merged.update(_condizioni)
    if not merged.has_key(nome):
        raise CondizioneNonValidaError("Condizione sconosciuta: "+str(nome))
    
    classe = merged[nome]
    
    if classe.startswith("."):
        classe = classe[1:]
        classe = "icse.ps.rules.condizioni."+classe+"."+classe
        
    return new_object_from_complete_classname(classe, args)

class CondizioneNonValidaError(Exception):
    pass