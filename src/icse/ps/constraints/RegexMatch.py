'''
Created on 27/mar/2012

@author: ximarx
'''
from icse.ps.Constraint import Constraint
import re

class RegexMatch(Constraint):
    
    _flag_resolver = {
        re.IGNORECASE : 'i|I|IGNORECASE',
        re.LOCALE: 'l|L|LOCALE',
        re.UNICODE: 'u|U|UNICODE',
        re.MULTILINE: 'm|M|MULTILINE',
        re.DOTALL: 's|S|DOTALL',
        re.VERBOSE: 'x|X|VERBOSE'
    }
    
    for (k,v) in _flag_resolver.items():
        _flag_resolver.update(dict([(vv, k) for vv in v.split('|')]))
        del _flag_resolver[k]
    
    
    '''
    Impone una regex match su un valore stringa
    '''
    def __init__(self, regex, flags = None):
        '''
        Constructor
        '''
        if flags == None:
            flags = []
        
        self._regex = regex
        self._flags = flags
        
    def to_json(self):
        updated = Constraint.to_json(self)
        updated.update({
                'regex' : self._regex,
                'flags' : self._flags
            })
        return updated
        
    def _resolve_flag(self, key):
        if RegexMatch._flag_resolver.has_key(key):
            return RegexMatch._flag_resolver[key]
        else:
            return 0
        
    def is_valid(self, value):
        flags = 0
        for val in self._flags:
            flags = flags | self._resolve_flag(val)
        p = re.compile(self._regex, flags)
        m = p.match(value)
        if m:
            return True
        else:
            return False