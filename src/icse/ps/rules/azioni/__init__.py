from icse.ps.rules.azioni.Azione import Azione
from icse.ps.Utils import new_object_from_complete_classname

__all__ = [ 'azioni', 'factory', 'AzioneNonValidaError' ]

_azioni = {
        'asserisci': '.Asserisci',
        'ritratta': '.Ritratta',
        'cambiaFatto': '.CambiaFatto',
        'disabilitaRegolaPer': '.DisabilitaRegolaPer',
        'mostraMessaggio': '.MostraMessaggio'
    }

def azioni():
    return  _azioni.keys()

def factory(nome, args = None):
    if args == None:
        args = []
    if not _azioni.has_key(nome):
        raise AzioneNonValidaError("Azione sconosciuta: "+str(nome))
    
    classe = _azioni[nome]
    
    if classe.startswith("."):
        classe = classe[1:]
        classe = "icse.ps.rules.azioni."+classe+"."+classe
        
    return new_object_from_complete_classname(classe, args)
    


class AzioneNonValidaError(Exception):
    pass