from mycode.fibonacci_series import fibonacci_series


def test_fibonacci_six_numbers():
    assert fibonacci_series(6) == [0, 1, 1, 2, 3, 5]


def test_fibonacci_five_numbers():
    assert fibonacci_series(5) == [0, 1, 1, 2, 3]


def test_fibonacci_one_number():
    assert fibonacci_series(1) == [0]


def test_fibonacci_zero():
    assert fibonacci_series(0) == []