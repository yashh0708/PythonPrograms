from mycode.reverse_number import reverse_number


def test_reverse_number():
    assert reverse_number(1234) == 4321


def test_reverse_three_digit_number():
    assert reverse_number(123) == 321


def test_reverse_single_digit():
    assert reverse_number(5) == 5


def test_reverse_number_with_zero():
    assert reverse_number(120) == 21