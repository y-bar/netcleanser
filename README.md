# netcleanser

A simple library to cleaning up url and email address.

![ci](https://github.com/y-bar/netcleanser/workflows/ci/badge.svg?branch=master)
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
>>> email.is_valid()
True
>>> email.value
'shinichi.takayanagi@gmail.com'
```

This `Email` class is `settable` and `dictable`
```python
# As dict
>>> x = {email: 1}
>>> x[email]
1
# As set
>>> {Email.build(), email, email, email}
{Email(value='shinichi.takayanagi@gmail.com)', Email(value='dummy@dummy.com)'}
```
