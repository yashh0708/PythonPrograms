from mycode.even_odd import even_odd


def test_even_number():
    assert even_odd(10) == "Even"


def test_odd_number():
    assert even_odd(7) == "Odd"


def test_another_even_number():
    assert even_odd(4) == "Even"


def test_negative_odd_number():
    assert even_odd(-5) == "Odd"


def test_negative_even_number():
    assert even_odd(-4) == "Even"