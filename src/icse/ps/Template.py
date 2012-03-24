'''
Created on 24/mar/2012

@author: ximarx
'''
from icse.ps.Fact import Fact

class Template :
    '''
    Una definizione di template di fatto:
    permette di specificare requisiti o limiti
    sugli attributi dei fatti
    '''


    def __init__(self, symbol, attributes = []):
        '''
        Constructor
        '''
        self.__id = symbol
        self.__attributes = attributes
        
    def get_id(self):
        return self.__id
    
    def set_id(self, symbol):
        self.__id = symbol
        
    def append_attribute(self, attribute):
        self.__attributes.append(attribute)
        
    def is_valid(self, fact):
        if not isinstance(fact, Fact):
            raise TypeError("Fact non e' un Fact")
        
        fact_attr = fact.get_attributes()
        
        for requirement in self.__attributes :
            has_attr = fact_attr.has_key(requirement.get_key())
            if requirement.is_required() and not has_attr :
                return False
            
            if has_attr :
                
                fact_val = fact_attr[requirement.get_key()]
                req_type = requirement.get_rtype()
                
                if req_type == Template.Attribute.TYPE_STRING :
                    if type(fact_attr[requirement.get_key()]) != str:
                        return False
                elif req_type == Template.Attribute.TYPE_FLOAT :
                    if type(fact_attr[requirement.get_key()]) != float:
                        return False
                elif req_type == Template.Attribute.TYPE_BOOLEAN :
                    if type(fact_attr[requirement.get_key()]) != bool:
                        return False
                elif req_type == Template.Attribute.TYPE_INT :
                    if type(fact_attr[requirement.get_key()]) != int:
                        return False
                elif req_type == Template.Attribute.TYPE_SET :
                    if requirement.get_attributes().count(fact_val) < 1 :
                        return False
                else:
                    raise TypeError("typeAttr sconosciuto")

                 
              
        return True
        
    class Attribute :
        '''
        Rappresenta una condizione imposta
        '''
        
        TYPE_STRING = 0
        TYPE_INT = 1
        TYPE_FLOAT = 2
        TYPE_SET = 3
        TYPE_BOOLEAN = 4
        TYPE_REGEX = 5
        
        def __init__(self, key, required = False, typeAttr = TYPE_STRING, attributes = {}):
            self.__key = key
            self._type = type
            self.__required = required
            self.__attributes = attributes
            
        def set_key(self, key):
            self.__key = key
            
        def set_required(self, required):
            self.__required = required
            
        def set_type(self, typeAttr):
            self._type = type
            
        def set_attributes(self, attributes):
            self.__attributes = attributes
            
        def is_required(self):
            return (self.__required == True)
        
        def get_key(self):
            return self.__key
        
        def get_rtype(self):
            return self._type
        
        def get_attributes(self):
            return self.__attributes
        
            