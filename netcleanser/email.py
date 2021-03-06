import re
from loguru import logger
from typing import Optional

# Thanks!
# https://gist.github.com/neu5ron/66078f804f16f9bda828
DOMAIN_NAME_REGEX: re.Pattern = re.compile(r'(([\da-zA-Z])([_\w-]{,62})\.){,127}(([\da-zA-Z])[_\w-]{,61})?([\da-zA-Z]\.((xn\-\-[a-zA-Z\d]+)|([a-zA-Z\d]{2,})))', re.IGNORECASE)
USED_NETCLENSER_EMAIL_INSIDE_ONLY: str = "used_netcleanser_email_inside_only"

def _looks_domain(x: str) -> bool:
    domain_name = x.lower().strip()
    return True if re.match(DOMAIN_NAME_REGEX, x) else False

def _automatic_correction(email: str) -> str:
    return email.replace("＠", "@")

class Email:
    def __init__(self, value: str):
        self._value = _automatic_correction(value)
        self._local_part, self._domain = self._value.split('@')
 
    def __str__(self) -> str:
        return self._value

    def __repr__(self) -> str:
        # The same format with dataclass ;)
        return f"Email(value='{self._value})'"

    def __eq__(self, other) -> bool:
        if not isinstance(other, Email):
            return False
        return self._value == other._value
    
    def __hash__(self) -> int:
        return hash(self._value)

    @property
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
    def build(value: Optional[str] = USED_NETCLENSER_EMAIL_INSIDE_ONLY, local_part: str = "dummy", domain: str = "dummy.com") -> Optional['Email']:
        if value is None:
            return None

        if value != USED_NETCLENSER_EMAIL_INSIDE_ONLY:
            try:
                return Email(value)
            except Exception as e:
                logger.warning(e) 
                if _looks_domain(value):
                    return Email(f"@{value}")
                else:
                    return None
            return None

        return Email(f"{local_part}@{domain}")
