from mycode.primes_in_range import primes_in_range


def test_primes_from_one_to_ten():
    assert primes_in_range(1, 10) == [2, 3, 5, 7]


def test_primes_from_ten_to_twenty():
    assert primes_in_range(10, 20) == [11, 13, 17, 19]


def test_small_range():
    assert primes_in_range(1, 3) == [2, 3]

