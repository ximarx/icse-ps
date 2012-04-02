'''
Created on 02/apr/2012

@author: Francesco Capozzo
'''
import json
import os
from icse.ps.Template import Template
from icse.ps.facts import templates
from copy import copy

class Parser(object):
    '''
    Parser di template di regole
    '''

    def __init__(self):
        '''
        Constructor
        '''
        
    def load_file(self, filepath):
        
        loaded = json.load(open(filepath))
        tmpls = []
        
        for jsont in loaded:
            t = Template(jsont['id'])
            
            for (attr, jsonobj) in jsont['constraints'].items():
                t.add_constraint(attr, self._create_constraints(jsonobj), 'replace')
                
            tmpls.append(t)
            
        return tmpls
    
    def _create_constraints(self, jsonobj):
        
        c_type = jsonobj['type']
        obj = None
        if c_type in templates.constraints():
            args = copy(jsonobj)
            del args['type']
            obj = templates.factory(c_type, args)
        elif c_type in templates.chains() :
            obj = templates.factory(c_type, [[self._create_constraints(x) for x in jsonobj['constraints']]])
            
        return obj
        
        
        
if __name__ == '__main__':
    
    
    p = Parser()
    loaded = p.load_file(os.getcwd()+'/../../../../../games/8/templates.json')
    

    print "[" + ",\n".join([str(x) for x in loaded]) + "]"
    