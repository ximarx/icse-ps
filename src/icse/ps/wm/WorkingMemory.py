'''
Created on 24/mar/2012

@author: ximarx
'''

class WorkingMemory(object):
    '''
    Base class per implementazione working memory
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
    def assert_fact(self, fact):
        '''
        Aggiunge un nuovo fatto alla working memory
        '''
        raise UnimplementedMethodError()
    
    def retract_fact(self, fact, template=None):
        '''
        Ritratta un nuovo fatto dalla working memory
        @param fact: Fact o id fatto
        @param template: se fact e' una string, usa template per filtrare il tipo 
        @return: icse.ps.Fact
        '''
        raise UnimplementedMethodError()
    
    def def_template(self, template):
        '''
        Definisce un nuovo tipo di template di fatti
        @param template: Template o template id
        @return: None
        '''
        raise UnimplementedMethodError()
    
    def get_templates(self):
        '''
        Restituisce una lista dei template di fatti registrati
        @return: collections[template]
        '''
        raise UnimplementedMethodError()
        
    def get_facts(self, template = None):
        '''
        Restituisce i fatti nella working memory
        (eventualmente filtrati in base al template)
        @param template: icse.ps.Template or string template
        @return: Fact[]
        '''
        raise UnimplementedMethodError()
    
    def __eq__(self, other):
        if not isinstance(other, WorkingMemory):
            return NotImplemented
        
        assert isinstance(other, WorkingMemory)
        
        sfacts = self.get_facts()
        ofacts = other.get_facts()
        
        # primo controllo su quantita di fatti
        if len(ofacts) != len(sfacts):
            return False
    
        for sfact in sfacts:
            if ofacts.count(sfact) != 1:
                return False
            
        return True
    
    def __ne__(self, other):
        return not self.__eq__(other, other)

    def __hash__(self):
        # correggere
        return 0
        
        

class FactNotFoundError(Exception):
    pass
        
        
class UnimplementedMethodError(Exception):
    pass
