from mycode.palindrome_number import is_palindrome_number


def test_palindrome_number():
    assert is_palindrome_number(121) is True


def test_not_palindrome_number():
    assert is_palindrome_number(123) is False


def test_another_palindrome():
    assert is_palindrome_number(1221) is True


def test_single_digit():
    assert is_palindrome_number(5) is True