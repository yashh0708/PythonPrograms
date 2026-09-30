from mycode.palindrome_string import is_palindrome_string


def test_palindrome_string():
    assert is_palindrome_string("madam") is True


def test_not_palindrome_string():
    assert is_palindrome_string("hello") is False


def test_another_palindrome():
    assert is_palindrome_string("level") is True


def test_single_character():
    assert is_palindrome_string("a") is True