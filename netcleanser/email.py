import re
from typing import Optional

def _automatic_correctionmodify(email: str):
    return email.replace("＠", "@")

class Email:
    def __init__(self, value: Optional[str] = None):
        self.value = None
        self.local_part = None
        self.domain = None
        try:
            self.value = _automatic_correctionmodify(value)
            self.local_part, self.domain = self.value.split('@')
            self.is_valid = True
        except:
            self.is_valid = False
 
    def __str__(self):
        return self.value

    def __repr__(self):
        return f"Email(value={self.value})"

    def __eq__(self, other):
        if not isinstance(other, Email):
            return False
        return self.value == other.value
    
    def __hash__(self):
        return hash(self.value)

    @staticmethod
    def build(local_part: str = "dummy", domain: str = "dummy.com"):
        return Email(f"{local_part}@{domain}")
