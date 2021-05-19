import purl
import requests

class Url():
    def __init__(self, url_str=None, host=None, username=None, password=None,scheme=None, port=None, path=None, query=None, fragment=None):
        self._purl = purl.URL(url_str, host, username, password, scheme, port, path, query, fragment)            
        
    # properties(e.g. netloc, scheme, host, domain, path, query)
    def __getattr__(self, name):
        return self._purl.__getattribute__(name)()

    @property
    def is_accessible(self, timeout = (1.0, 3.0)) -> bool:
        try:
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36"
            }
            r = requests.get(self.as_string(), headers=headers, timeout=timeout)
            r.raise_for_status()
        except Exception:
            return False
        return True

    @property
    def is_valid(self) -> bool:
        try:
            return all([self.scheme, self.netloc])
        except ValueError:
            return False

    def as_string(self):
        return self._purl.as_string()