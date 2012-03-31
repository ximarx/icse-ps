'''
Created on 30/mar/2012

@author: ximarx
'''
from icse.ps.rules.funzioni.Funzione import Funzione

class Proxy:
    '''
    Esegue una redirect della parte operativa degli 
    operandi "Funzione" verso l'implementazione reale
    '''

    '''
    il formato di funzioni una volta riempito:
        'nomefunzione1': {
                'handler': ref a un callable,
                'minParams: numero di parametri minimo
            },
        'nomefunzione2': ...
    '''
    _funzioni = {}

    _initied = False

    @staticmethod        
    def call(nome, args = []):
        '''
        Invoca una funzione presente nel dizionario
        di funzioni oppure lancia una eccezione se:
            - il tipo o il numero di argomenti
                attesi e' diverso dal richiesto
            - non c'e' una funzione con il nome richiesto
                nel dizionario di funzioni (che viene
                inizializzato all'importazione del package
        '''
        if not Proxy._funzioni.has_key(nome):
            raise FunzioneNonTrovataError("La funzione richiesta non e' definita: "+str(nome))
        
        func = Proxy._funzioni[nome]
        if func['minParams'] > len(args):
            raise FirmaNonRispettataError("Il numero minimo di parametri ("+func['minParams']+") per la funzione "+nome+" non e' stato rispettato: "+len(args)+" forniti")
        
        return func['handler'](*args)

        
    
    @staticmethod
    def define(funcName, handler, minParams = 0):
        if Proxy._funzioni.has_key(funcName):
            raise DefinizioneDuplicataError("Funzione gia definita: "+funcName)
        
        if not callable(handler):
            raise HandlerInvalidoError("L'handler fornito non e' valido")
        
        Proxy._funzioni[funcName] = {
                    'handler' : handler,
                    'minParams' : minParams
                }
        
    @staticmethod
    def initied():
        return Proxy._initied
    
    @staticmethod
    def set_initied():
        Proxy._initied = True
      
class ProxyError(Exception):
    '''
    Eccezione base lanciata dal Proxy
    '''
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)
        
class DefinizioneDuplicataError(ProxyError):
    '''
    Lanciata durante il tentativo di ridefinire
    una funzione gia definita
    '''

class HandlerInvalidoError(ProxyError):
    '''
    Lanciata quando l'handler fornito non e' valido
    '''

class FunzioneNonTrovataError(ProxyError):
    '''
    Lanciata se viene richiesta una funzione non
    presente nel dizionario
    '''
    
class FirmaNonRispettataError(ProxyError):
    '''
    Lanciata quando il numero minimo
    di parametri richiesto della funzione
    non e' rispettato
    '''

        