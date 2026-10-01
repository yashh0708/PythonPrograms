from mycode.second_largest import second_largest


def test_second_largest():
    assert second_largest([10, 5, 20, 8, 15]) == 15


def test_second_largest_simple():
    assert second_largest([1, 2, 3, 4]) == 3


def test_second_largest_with_duplicates():
    assert second_largest([10, 20, 20, 5]) == 10


def test_negative_numbers():
    assert second_largest([-10, -5, -20]) == -10