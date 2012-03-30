from icse.ps.rules.funzioni.Funzione import Funzione
from icse.ps.rules.funzioni.Proxy import Proxy

if not Proxy.initied():
    funzioni = [
        '.Somma',
        '.Prodotto',
        '.Sottrazione',
        '.Divisione',
        '.Potenza',
        '.Radice',
    ]
    
    for modulo in funzioni:
        if modulo.startswith("."):
            classe = modulo[1:]
            modulo = "icse.ps.rules.funzioni"+modulo
        else:
            lastdot = modulo.rfind('.')
            classe = modulo[lastdot+1:]
            modulo = modulo[0:lastdot]
        
        #print "Modulo: ",modulo
        #print "Classe: ",classe
            
        try:
            imported = __import__(modulo,  globals(), locals(), [classe], -1)
            attr = getattr(imported, classe)
        
            #print "Canonical: ",attr
        
            if issubclass(attr, Funzione):
                sign = attr.sign()
                Proxy.define(sign['sign'], sign['handler'], sign['minParams'])
        except Exception, e:
            raise
        
    Proxy.set_initied()

    #print Proxy._funzioni
    #print Proxy.call('potenza', [2,2])