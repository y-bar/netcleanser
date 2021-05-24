from netcleanser import Email


def test_email():
    # Normal cases
    for value in ["hoge.moge@gmail.com", "hoge.moge＠gmail.com"]:
        email = Email(value)
        assert email.is_valid == True
        assert email.local_part == "hoge.moge"
        assert email.domain == "gmail.com"
        assert str(email) == email.value
        assert Email.build(local_part = email.local_part, domain = email.domain) == email

def test_empty_local_part():
    for value in ["gmail.com", "@gmail.com"]:
        email = Email.build(value)
        assert email.is_valid == True
        assert email.local_part == ""
        assert email.domain == "gmail.com"
        assert str(email) == email.value
        assert Email.build(local_part = email.local_part, domain = email.domain) == email

def test_internationalized_domain():
    for value in ["あうふへぇ@ほげほげ.com", "あうふへぇ＠ほげほげ.com"]:
        email = Email(value)
        assert email.is_valid == True
        assert email.local_part == "あうふへぇ"
        assert email.domain == "ほげほげ.com"
        assert str(email) == email.value
        assert Email.build(local_part=email.local_part, domain = email.domain) == email

def test_email_is_invalid():
    for value in ["", "akdsjfkjh", 'javascript:void(0)', None]:
        assert Email.build(value) is None

def test_email_build():    
    email = Email.build(domain="hoge.com")
    assert email.local_part == "dummy"
    assert email.domain == "hoge.com"

    email = Email.build(local_part="hoge")
    assert email.local_part == "hoge"
    assert email.domain == "dummy.com"

    email = Email.build(value="hoge@gmail.com")
    assert email.local_part == "hoge"
    assert email.domain == "gmail.com"

def test_email_should_be_settable():
    {Email("hoge@gmail.com"), Email("xxx@yahooo")}

def test_email_should_be_dictable():
    d = {Email("hoge@gmail.com"): 123, Email("xxx@yahooo"): 456}
    assert d[Email("hoge@gmail.com")] == 123
