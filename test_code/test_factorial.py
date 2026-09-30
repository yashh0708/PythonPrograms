from mycode.factorial import factorial


def test_factorial_of_five():
    assert factorial(5) == 120


def test_factorial_of_three():
    assert factorial(3) == 6


def test_factorial_of_one():
    assert factorial(1) == 1


def test_factorial_of_zero():
    assert factorial(0) == 1