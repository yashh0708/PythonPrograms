from mycode.remove_duplicates import remove_duplicates


def test_remove_duplicates():
    assert remove_duplicates([1, 2, 2, 3, 3, 4]) == [1, 2, 3, 4]


def test_no_duplicates():
    assert remove_duplicates([1, 2, 3]) == [1, 2, 3]


def test_all_duplicates():
    assert remove_duplicates([5, 5, 5]) == [5]


def test_empty_list():
    assert remove_duplicates([]) == []