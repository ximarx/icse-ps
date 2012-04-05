'''
Created on 24/mar/2012

@author: ximarx
'''
import json

class Fact:
    '''
    Rappresentazione generica di un FATTO
    '''

    def __init__(self, symbol, attributes = None, template = None):
        '''
        Constructor
        '''
        if attributes == None:
            attributes = {}
        
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
    
    
    def __eq__(self, other):
        if not isinstance(other, Fact):
            return NotImplemented
        
        assert isinstance(other, Fact)
        
        if self.get_template() != other.get_template():
            return False
        
        if self.get_id() != other.get_id():
            return False
        
        sattr = self.get_attributes()
        oattr = other.get_attributes()
        
        if len(sattr) != len(oattr):
            return False
        
        for (s_k, s_v) in sattr.items():
            if not oattr.has_key(s_k):
                return False
            
            if s_v != oattr[s_k]:
                return False
            
        return True
    
    def __ne__(self, other):
        return not self.__eq__(other)
    
if __name__ == '__main__':

    f_main = Fact("uno", {"uno":1}, "gen")
    
    uguale = Fact("uno", {"uno":1}, "gen")
    div_piu_un_attr = Fact("uno", {"uno":1, "due":2}, "gen")
    div_meno_un_attr = Fact("uno", {}, "gen")
    div_id = Fact("due", {"uno":1}, "gen")
    div_tmpl = Fact("uno", {"uno":1}, "spec")
    
        
    print "fmain == uguale ? ", (f_main == uguale)
    print "fmain == div_piu_un_attr ? ", (f_main == div_piu_un_attr)    
    print "fmain == div_meno_un_attr ? ", (f_main == div_meno_un_attr)
    print "fmain == div_id ? ", (f_main == div_id)
    print "fmain == div_tmpl ? ", (f_main == div_tmpl)
    
    print "fmain != uguale ? ", (f_main != uguale)
    print "fmain != div_piu_un_attr ? ", (f_main != div_piu_un_attr)    
    print "fmain != div_meno_un_attr ? ", (f_main != div_meno_un_attr)
    print "fmain != div_id ? ", (f_main != div_id)
    print "fmain != div_tmpl ? ", (f_main != div_tmpl)
    
    