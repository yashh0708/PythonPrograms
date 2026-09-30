from mycode.prime_number import is_prime


def test_prime_number():
    assert is_prime(7) is True


def test_not_prime_number():
    assert is_prime(10) is False


def test_two_is_prime():
    assert is_prime(2) is True


def test_one_is_not_prime():
    assert is_prime(1) is False