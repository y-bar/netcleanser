from netcleanser import Url
import urllib



def test_valid_url():
    url_string = 'https://www.google.com/search?q=testing'
    url = Url(url_string)
    assert url.scheme == 'https'
    assert url.host == 'www.google.com'
    assert url.domain == 'www.google.com'
    assert url.registered_domain == 'google.com'
    assert url.netloc == 'www.google.com'
    assert url.path == '/search'
    assert url.query == 'q=testing'
    assert url.is_valid == True
    assert url.is_accessible == True
    assert url.value == url_string
    assert url == Url(url_string)
    assert str(url) == url_string
    assert url != url_string
    assert url.contains_www == True
    assert url.remove_www() == Url('https://google.com/search?q=testing')
    assert url.remove_query() == Url('https://www.google.com/search')
    hash(url) 


def test_invalid_url():
    url = Url('https://goooooooooooogle.com')
    assert url.is_accessible == False
    assert url.contains_www == False
    assert url.add_www() == Url('https://www.goooooooooooogle.com')

def test_invalid_url_2():
    url = Url.build('javascript:void(0)')
    assert url is None


def test_remove_query():
    url_string = 'https://www.google.com/search'
    query_string = "p=testing&q=hoge&q=moge"
    url = Url(url_string + "?" + query_string)
    assert url.remove_query() == Url(url_string)
    assert url.remove_query("p") == Url(url_string + "?q=hoge&q=moge")
    assert url.remove_query("p", "testing") == Url(url_string + "?q=hoge&q=moge")
    assert url.remove_query("q") == Url(url_string + "?p=testing")
    assert url.remove_query("q", "moge") == Url(url_string + "?p=testing&q=hoge")


def test_url_should_be_settable():
    {Url("https://www.google.com"), Url("https://www.google.co.jp")}


def test_url_should_be_dictable():
    d = {Url("https://www.google.com"): 123, Url("https://www.google.co.jp"): 456}
    assert d[Url("https://www.google.co.jp")] == 456
