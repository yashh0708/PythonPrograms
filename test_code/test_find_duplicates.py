from mycode.find_duplicates import find_duplicates


def test_find_duplicates():
    assert find_duplicates([1, 2, 3, 2, 4, 3]) == [2, 3]


def test_one_duplicate():
    assert find_duplicates([1, 2, 2, 3]) == [2]


def test_no_duplicates():
    assert find_duplicates([1, 2, 3, 4]) == []


def test_multiple_duplicates():
    assert find_duplicates([1, 1, 2, 2, 3, 3]) == [1, 2, 3]