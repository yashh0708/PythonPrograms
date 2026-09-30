from mycode.largest_of_three import largest_of_three


def test_largest_number():
    assert largest_of_three(10, 20, 15) == 20


def test_first_number_largest():
    assert largest_of_three(30, 20, 10) == 30


def test_third_number_largest():
    assert largest_of_three(10, 20, 30) == 30


def test_equal_numbers():
    assert largest_of_three(5, 5, 5) == 5