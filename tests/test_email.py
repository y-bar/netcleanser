from netcleanser import Email


def test_email_1():
    email = Email("hoge.moge@gmail.com")
    assert email.local_part == "hoge.moge"
    assert email.domain == "gmail.com"
