from netcleanser import Url


def test_valid_url():
    url_string = 'https://www.google.com/search?q=testing'
    url = Url(url_string)
    assert url.scheme == 'https'
    assert url.host == 'www.google.com'
    assert url.domain == 'www.google.com'
    assert url.netloc == 'www.google.com'
    assert url.path == '/search'
    assert url.query == 'q=testing'
    assert url.is_valid == True
    assert url.is_accessible == True
    assert url.value == url_string
    assert str(url) == url_string
    assert url == Url(url_string)
    assert url != "aaaa"
    hash(url) 


def test_invalid_url():
    url = Url('https://goooooooooooogle.com')
    assert url.is_accessible == False


def test_url_should_be_settable():
    {Url("https://www.google.com"), Url("https://www.google.co.jp")}


def test_url_should_be_dictable():
    d = {Url("https://www.google.com"): 123, Url("https://www.google.co.jp"): 456}
    assert d[Url("https://www.google.co.jp")] == 456
