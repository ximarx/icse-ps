'''
Created on 31/mar/2012

@author: Francesco Capozzo
'''
from icse.ps.rules.azioni.Azione import Azione
from icse.ps.rules.operandi.Operando import Operando
from icse.ps.Fact import Fact

class Asserisci(Azione):
    '''
    Aggiunge un nuovo fatto alla WorkingMemory
    '''

    def __init__(self, idfatto, template, attributi):
        '''
        Constructor
        '''
        assert isinstance(idfatto, Operando) or isinstance(idfatto, "".__class__), \
            "Atteso idfatto di tipo Operando o string, fornito: "+str(type(idfatto))
        assert isinstance(template, Operando) or isinstance(template, "".__class__), \
            "Atteso template di tipo Operando o string, fornito: "+str(type(template))
        assert isinstance(attributi, Operando) or isinstance(attributi, dict), \
            "Atteso attributi di tipo Operando o dict, fornito: "+str(type(attributi))
            
        self._idfatto = idfatto
        self._template = template
        self._attributi = attributi
        
    def esegui(self, wm, simboli, agenda):
        '''
        Esegue la modifica di un attributo di un fatto
        '''
        '''chiamo il metodo base per il controllo dei parametri'''
        Azione.esegui(self, wm, simboli, agenda)
        
        '''risolvo idfatto'''
        vidfatto = self._idfatto
        if isinstance(vidfatto, Operando):
            vidfatto = vidfatto.valuta(self, simboli)
            
        '''risolvo template'''
        vtemplate = self._template
        if isinstance(vtemplate, Operando):
            vtemplate = vtemplate.valuta(self, simboli)
            
        '''risolvo attributi'''
        vattributi = self._attributi
        if isinstance(vattributi, Operando):
            vattributi = vattributi.valuta(self, simboli)
            
        '''tutto e' pronto per l'esecuzione'''
        assert isinstance(vattributi, dict), \
            "Atteso attributi di tipo dict dopo la valutazione, ottenuto: "+str(type(vattributi))
             
        wm.assert_fact( Fact(vidfatto, vattributi, vtemplate))
        
    def __str__(self):
        return " ".join([
                'asserisci fatto',
                str(self._idfatto),
                'di tipo',
                str(self._template),
                'con attributi',
                str(self._attributi)
            ])
