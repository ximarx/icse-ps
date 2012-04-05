'''
Created on 24/mar/2012

@author: ximarx
'''
from icse.ps.constraints.AndChain import AndChain
from icse.ps.constraints.OrChain import OrChain
from icse.ps.constraints.XorChain import XorChain
import json
from icse.ps.Constraint import Constraint
from icse.ps.Fact import Fact

class Template(object) :
    '''
    Una definizione di template di fatto:
    permette di specificare requisiti o limiti
    sugli attributi dei fatti
    '''


    def __init__(self, templateId, constraints = None):
        '''
        Constructor
        '''
        if constraints == None:
            constraints = {}
        self._templateId = templateId
        self._constraints = constraints
        
    def add_constraint(self, attrName, constraint, conjuction = 'and' ):
        '''
        Aggiunge una condizione su un attributo.
        Se esiste gia una condizione sullo stesso attributo
        verranno congiunte attraverso una AndChain o una OrChain
        o una XorChain in base al valore di conjuction
        
        Usa fluent interface
        
        @param attrName: str
        @param constraint: icse.ps.Constraint.Constraint
        @param conjuction: and|or|xor|% per replace della vecchia condizione (se presente)
        @return: icse.ps.Template.Template
        '''
        
        if not isinstance(constraint, Constraint) :
            raise TypeError("Atteso constraint di tipo Contraint, "+constraint.__class__.__name__+" passato")
        
        if self._constraints.has_key(attrName) :
            #dobbiamo inserire la nuova in una chain
            currentConstraint = self._constraints[attrName]
            if conjuction == 'and':
                #unisce con and
                constraint = AndChain([currentConstraint, constraint])
            elif conjuction == 'or':
                #unisce con or
                constraint = OrChain([currentConstraint, constraint])
            elif conjuction == 'xor':
                #unisce con xor
                constraint = XorChain([currentConstraint, constraint])
            #else:
                #ripristina la vecchia rule (lo fa senza l'else)
        
        self._constraints[attrName] = constraint
        return self
        
    def get_templateid(self):
        '''
        Getter per templateId
        '''
        return self._templateId
    
    def set_templateid(self, templateId):
        '''
        Setter per templateId
        @return: icse.ps.Template.Template
        '''
        self._templateId = templateId
        return self
        
    def __str__(self):
        #const_fmted = dict([(k,v.to_json()) for (k,v) in self._constraints.iteritems()])
        return json.dumps({
                'id': self.get_templateid(),
                'constraints': dict([(k,v.to_json()) for (k,v) in self._constraints.iteritems()])
            }, indent=4)
        
    def validate(self, fact, raiseOnInvalid = True, removeUnknown = False ):
        '''
        Convalida un fatto secondo questo template
        E' possibile alterare il comportamento del validatore
        nel caso di elementi invalidi o sconosciuti
        nel fatto tramite i parametri
        
        @param fact: icse.ps.Fact.Fact
        @param raiseOnInvalid: boolean indica se terminare la validazione 
            al primo elemento non valido o se continuare comunque
        @param removeUnknown: boolean rimuovere gli attributi sconosciuti 
            a questo template prima di eseguire una validazione
        @return booleam
        @raise InvalidFactAttributeError: se uno degli attributi del fatto
             non rispetta le specifiche definite dal template e raiseOnInvalid
             e' definito vero
        @raise TypeError: se fact non e' di tipo icse.ps.Fact.Fact 
        '''
        
        if not isinstance(fact, Fact):
            raise TypeError("Atteso fact di tipo Fact, "+fact.__class__.__name__+" passato")

        if removeUnknown :
            for key in fact.get_attributes().keys():
                if not self._constraints.has_key(key):
                    del fact[key]
        
        is_valid = True
        
        for attr, consts in self._constraints.items():
            if not consts.is_valid(fact[attr]):
                if raiseOnInvalid:
                    raise InvalidFactAttributeError("Valore dell'attributo {"+str(attr)+"} non valido: "+str(fact[attr]))
                is_valid = False 
            
        return is_valid
            
           
           
class InvalidFactAttributeError(Exception):
    pass
        
        