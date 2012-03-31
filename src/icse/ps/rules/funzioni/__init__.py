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
        '.Attributo'
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
    
if __name__ == '__main__':
    print "--- Test su Proxy e funzioni ---"
    print
    
    success = 0
    failure = 0
    
    def _test_handler(op1):
        return "Mi hai passato: "+str(op1)
    
    try:
        print "Testo aggiunta nuova funzione..."
        Proxy.define('_test_handler', _test_handler, 1)
        print "\tOk"
        success += 1
    except Exception, e:
        print "\tFallito"
        failure += 1
    
    try:
        print "Testo ridefinizione di funzione gia presente..."
        Proxy.define('_test_handler', _test_handler, 2)
        print "\tFallito"
        failure += 1
    except Exception, e:
        print "\tOk"
        success += 1
        
    try:
        print "Testo chiamata a funzione _test_handler('prova')..."
        if Proxy.call('_test_handler', ['prova']) == 'Mi hai passato: prova':
            print "\tOk"
            success += 1
        else:
            print "\tFallito"
            failure += 1
    except Exception, e:
        print "\tFallito, eccezione: " + str(e)
        failure += 1

    print "Testo funzioni build-in..."

    from icse.ps.Fact import Fact

    funzioni = [
        ('.Somma',
            ['somma', # <-- nome funzione test
                [1,2], # <-- operandi
            3] # <-- risultato atteso
        ),
        ('.Prodotto',
            ['prodotto', [2,3], 6]
         ),
        ('.Sottrazione',
            ['sottrazione', [3,1], 2]
         ),
        ('.Divisione',
            ['divisione', [6,3], 2]
         ),
        ('.Potenza',
            ['potenza', [10,2], 100]
         ),
        ('.Radice',
            ['radice', [81,2], 9]
         ),
        ('.Attributo',
            ['attributo', [Fact('test', {'x':True}),'x'], True]
         ),
    ]
    
    
    for (modulo, test) in funzioni:
        try:
            print "\tTesto classe: " + modulo
            if Proxy.call(test[0], test[1]) == test[2]:
                print "\t\tOk"
                success += 1
            else:
                print "\t\tFallito"
                failure += 1
        except Exception, e:
            print "\t\tFallito, eccezione: " + str(e)
            failure += 1
    
    
    print
    print "Risultati:"
    print "    Test eseguiti: " + str( (success + failure) )
    print "        Successi: " + str(success) + " (" + str( (((success+0.)/(success + failure)) * 100) )[0:4] + ")"
    print "        Fallimenti: " + str(failure)  + " (" + str( (((failure+0.)/(success + failure)) * 100) )[0:4] + ")"