from mycode.sum_of_digits import sum_of_digits


def test_sum_of_digits():
    assert sum_of_digits(1234) == 10


def test_sum_three_digits():
    assert sum_of_digits(123) == 6


def test_single_digit():
    assert sum_of_digits(5) == 5


def test_zero():
    assert sum_of_digits(0) == 0