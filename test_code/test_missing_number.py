from mycode.missing_number import find_missing_number


def test_missing_number():
    assert find_missing_number([1, 2, 3, 5]) == 4


def test_missing_number_two():
    assert find_missing_number([1, 2, 4, 5]) == 3


def test_missing_number_one():
    assert find_missing_number([2, 3, 4, 5]) == 1


def test_missing_number_last():
    assert find_missing_number([1, 2, 3, 4]) == 5