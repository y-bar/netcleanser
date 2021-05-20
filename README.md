# netcleanser

The library makes parsing and manipulation of URL🌐 and Email address📧 easy.

[![ci](https://github.com/y-bar/netcleanser/actions/workflows/ci.yml/badge.svg)](https://github.com/y-bar/netcleanser/actions/workflows/ci.yml)
[![license](https://img.shields.io/github/license/y-bar/netcleanser.svg)](https://github.com/y-bar/netcleanser/blob/master/LICENSE)
[![release](https://img.shields.io/github/release/y-bar/netcleanser.svg)](https://github.com/y-bar/netcleanser/releases/latest)


## Install

```bash
pip install netcleanser
```

## How to use

### Email 

```python
>>> from netcleanser import Email
>>> email = Email('shinichi.takayanagi@gmail.com')
>>> email.domain
'gmail.com'
>>> email.local_part
'shinichi.takayanagi'
>>> email.is_valid
True
>>> email.value
'shinichi.takayanagi@gmail.com'
```

This `Email` class is `settable` and `dictable`
```python
# As a dict key
>>> x = {email: 1}
>>> x[email]
1
# As elemtns of set
>>> email2 = Email("nakamichiworks@gmail.com")
>>> {email, email, email, email2, email2}
{Email(value='nakamichiworks@gmail.com)', Email(value='shinichi.takayanagi@gmail.com)'}
```

`Email.build()` allows you to create dummy email address specifing the only part of `local_part` or `domain`

```python
>>> Email.build(local_part = "hoge")
Email(value='hoge@dummy.com)'
>>> Email.build(domain = "hoge.com")
Email(value='dummy@hoge.com)'
```

### Url

```python
>>> from netcleanser import Url
>>> url = Url('https://www.google.com/search?q=auhuhe')
>>> assert url.scheme == 'https'
>>> url.scheme
'https'
>>> url.host
'www.google.com'
>>> url.domain
'www.google.com'
>>> url.netloc
'www.google.com'
>>> url.path
'/search'
>>> url.query
'q=auhuhe'
>>> url.is_valid
True
>>> url.is_accessible
True
>>> url.value
'https://www.google.com/search?q=auhuhe'
>>> str(url)
'https://www.google.com/search?q=auhuhe'
```

This `Url` class is `settable` and `dictable`
```python
>>> x = {url: 123}
>>> x[Url('https://www.google.com/search?q=auhuhe')]
123
>>> {url, url, Url('https://google.com'), url}
{_URLTuple(host='google.com', username=None, password=None, scheme='https', port=None, path='', query='', fragment=''), _URLTuple(host='www.google.com', username=None, password=None, scheme='https', port=None, path='/search', query='q=auhuhe', fragment='')}
```
