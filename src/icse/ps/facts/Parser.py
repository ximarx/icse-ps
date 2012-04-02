'''
Created on 02/apr/2012

@author: Francesco Capozzo
'''
from icse.ps.Fact import Fact
import json
import os

class Parser(object):
    '''
    Parser di fatti
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
    def load_file(self, filepath):
        
        loaded = json.load(open(filepath))
        
        facts = [Fact(jsonf['id'], jsonf['attributes'], jsonf['template']) for jsonf in loaded]
            
        return facts
        
        
if __name__ == '__main__':
    
    p = Parser()
    loaded = p.load_file(os.getcwd()+'/../../../../games/8/facts.json')
    

    print "[" + ",\n".join([str(x) for x in loaded]) + "]"
        