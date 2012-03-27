'''
Created on 24/mar/2012

@author: ximarx
'''
import json

class Fact:
    '''
    Rappresentazione generica di un FATTO
    '''

    def __init__(self, symbol, attributes = {}, template = None):
        '''
        Constructor
        '''
        for key, value in attributes.items() :
            setattr(self, key, value)
            
        self.set_id(symbol).set_template(template)
        
    def set_id(self, symbol):
        self.__id = symbol
        return self
    
    def get_id(self):
        return self.__id

    def set_template(self, template):
        self.__template = template
        return self
        
    def get_template(self):
        return self.__template
        
    def get_attributes(self):
        attributes = {}
        for name in dir(self):
            attr = getattr(self, name)
            if not callable(attr) and name[0:1] != "_" :
                attributes[name] = attr
        return attributes
    
    def __getitem__(self, key):
        '''
        permette di utilizzare fact[attr]
        '''
        if key[0:1] == '_':
            raise TypeError("Chiave non valida")
        return getattr(self, key)

    def __setitem__(self, key, value):
        '''
        permette di avvalorare fact[attr]
        '''
        if key == 'id' or key == 'template' or key[0:1] == '_':
            raise TypeError("Chiave non valida")
        return setattr(self, key, value)

    def __delitem__(self, key):
        '''
        permette di cancellare fact[attr]
        '''
        if key == 'id' or key == 'template' or key[0:1] == '_':
            raise TypeError("Chiave non valida")
        return delattr(self, key)


                 
    def __str__(self):
        return json.dumps({'id': self.get_id(), 'template': self.get_template(), 'attributes': self.get_attributes()}, indent=4)