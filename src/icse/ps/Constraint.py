'''
Created on 27/mar/2012

@author: ximarx
'''
import json

class Constraint:
    '''
    Rappresenta una condizione su un attributo
    all'interno di un template di fatti.
    Questa e' una classe base che dovrebbe
    essere estesa per aumentarne la semantica
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
        
    def to_json(self):
        jsonrep = {
                'type' : self.__module__+"."+self.__class__.__name__
            }
        return jsonrep
        
    def __str__(self):
        jsonstr = json.dumps(self.to_json(), indent=4)
        return jsonstr
    
    def is_valid(self, value):
        return True