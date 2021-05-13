import re
from typing import Optional, Final

# Thanks!
# https://gist.github.com/neu5ron/66078f804f16f9bda828
DOMAIN_NAME_REGEX: Final[str] = re.compile(r'(([\da-zA-Z])([_\w-]{,62})\.){,127}(([\da-zA-Z])[_\w-]{,61})?([\da-zA-Z]\.((xn\-\-[a-zA-Z\d]+)|([a-zA-Z\d]{2,})))', re.IGNORECASE)

def _looks_domain(x: str) -> bool:
    domain_name = x.lower().strip().encode('ascii')
    return True if re.match(DOMAIN_NAME_REGEX, x) else False

def _automatic_correction(email: str) -> str:
    return email.replace("＠", "@")

class Email:
    def __init__(self, value: Optional[str] = None):
        self._set_to_none()
        if value is None:
            return 
        try:
            self._value = _automatic_correction(value)
            self._local_part, self._domain = self._value.split('@')
        except:
            if _looks_domain(value):
                self._local_part = ""
                self._domain = value
                self._value = f"@{self._domain}"
            else:
                self._set_to_none()

    def _set_to_none(self):
        self._value = None
        self._local_part = None
        self._domain = None
 
    def __str__(self):
        return self._value

    def __repr__(self):
        # The same format with dataclass ;)
        return f"Email(value='{self._value})'"

    def __eq__(self, other):
        if not isinstance(other, Email):
            return False
        return self._value == other._value
    
    def __hash__(self):
        return hash(self._value)

    def is_valid(self) -> bool:
        return (self._value is not None)

    @property
    def domain(self) -> str:
        return self._domain

    @property
    def value(self) -> str:
        return self._value

    @property
    def local_part(self) -> str:
        return self._local_part

    @staticmethod
    def build(local_part: str = "dummy", domain: str = "dummy.com"):
        return Email(f"{local_part}@{domain}")
