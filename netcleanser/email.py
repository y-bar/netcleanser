import re

def _automatic_correctionmodify(email):
    return email.replace("＠", "@")

class Email:
    def __init__(self, email):
        self.email = _automatic_correctionmodify(email)
        self.local_part = None
        self.domain = None
        try:
            self.local_part, self.domain = self.email.split('@')
            self.is_valid = True
        except:
            self.is_valid = False

    
