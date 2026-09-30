from mycode.pos_neg_zero import check_number


def test_positive_number():
    assert check_number(10) == "Positive"


def test_negative_number():
    assert check_number(-10) == "Negative"


def test_zero():
    assert check_number(0) == "Zero"


def test_another_positive_number():
    assert check_number(25) == "Positive"