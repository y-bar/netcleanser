import re

def _automatic_correctionmodify(email):
    return email.replace("＠", "@")

class Email:
    def __init__(self, value):
        self.value = _automatic_correctionmodify(value)
        self.local_part = None
        self.domain = None
        try:
            self.local_part, self.domain = self.value.split('@')
            self.is_valid = True
        except:
            self.is_valid = False
 
    def __str__(self):
        return self.value

    def __eq__(self, other):
        if not isinstance(other, Email):
            return False
        return self.value == other.value
    
    def __hash__(self):
        return hash(self.value)
