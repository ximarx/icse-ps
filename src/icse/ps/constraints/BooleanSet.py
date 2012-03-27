'''
Created on 27/mar/2012

@author: ximarx
'''
from icse.ps.constraints.ValuesSet import ValuesSet

class BooleanSet(ValuesSet):
    '''
    Condizione di valore Booleano,
    in concreto un set di valori [0,1,true,false,True,False,T,F,t,f]
    '''


    def __init__(self):
        '''
        Constructor
        '''
        ValuesSet.__init__(self, [0,1,'0','1','true','false','True','False',True,False,'T','F','t','f'])
    
