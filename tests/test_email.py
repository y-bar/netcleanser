from netcleanser import Email


def test_email_1():
    email = Email("hoge.moge@gmail.com")
    assert email.local_part == "hoge.moge"
    assert email.domain == "gmail.com"

def test_email_2():
    email = Email(None)
    assert email.local_part is None
    assert email.domain is None
    assert email.value is None

def test_email_should_be_settable():
    xs = {Email("hoge@gmail.com"), Email("xxx@yahooo")}
