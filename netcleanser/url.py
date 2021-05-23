import re
import purl
import copy
import requests
import tldextract
from typing import Optional

# Regular expressions to remove "www.", "www1.", www123. etc."
WWW: re.Pattern = re.compile(r"^www[0-9]*\.")
# scheme e.g.: hoge://
SCHEME: re.Pattern = re.compile(r"^[A-Za-z0-9+.\-]+://")

class Url:
    def __init__(self, url_string: Optional[str] = None, host=None, username=None, password=None,scheme=None, port=None, path=None, query=None, fragment=None):
        # Add scheme enforcely if it is needed
        if url_string is not None and not re.search(SCHEME, url_string):
            url_string = f"http://{url_string}"
        self._purl = purl.URL(url_string, host, username, password, scheme, port, path, query, fragment)            

    def __getattr__(self, name):
        if name in ["netloc", "scheme", "host", "domain", "path", "query"]:
            return getattr(self._purl, name)()
        else:
            raise AttributeError(f"'Url' object has no attribute '{name}'")
    
    def __repr__(self):
        p = self._purl
        return f"Url(host='{p.host()}', username='{p.username()}', password='{p.password()}', scheme='{p.scheme()}', port='{p.port()}', path='{p.path()}', query='{p.query()}', fragment='{p.fragment()}')"

    def __str__(self):
        return self.value

    def __eq__(self, other):
        if not isinstance(other, Url):
            return False
        return self._purl.__eq__(other._purl)

    def __hash__(self):
        return self._purl.__hash__()


    def add_www(self) -> "Url":
        if self.contains_www:
            # Just retun the copy
            return Url(self.value)   
        return _mutate(self, host = "www." + self.host)

    def remove_www(self) -> "Url":
        host = re.sub(WWW, "", self.host)
        return _mutate(self, host = host)

    def remove_query(self, key=None, value=None) -> "Url":
        if key is not None:
            return Url(self._purl.remove_query_param(key, value).as_string())
        # Remove all, copy just in case
        purl = copy.copy(self._purl)
        for key, values in self._purl.query_params().items():
            for value in values:
                purl = purl.remove_query_param(key, value)
        return Url(purl.as_string())

    @property
    def contains_www(self) -> bool:
        return True if WWW.match(self.netloc) else False

    @property
    def value(self) -> str:
        return self._purl.as_string()

    @property
    def registered_domain(self) -> str:
        return tldextract.extract(self.value).registered_domain

    @property
    def is_accessible(self, timeout = (1.0, 3.0)) -> bool:
        try:
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36"
            }
            r = requests.get(self.value, headers=headers, timeout=timeout)
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


def _mutate(url: Url, **kwargs) -> Url:
    args = url._purl._tuple._asdict()
    args.update(kwargs)
    return Url(purl.URL(**args).as_string())
