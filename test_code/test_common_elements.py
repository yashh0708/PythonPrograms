from mycode.common_elements import common_elements


def test_common_elements():
    assert common_elements([1, 2, 3, 4], [3, 4, 5, 6]) == [3, 4]


def test_one_common_element():
    assert common_elements([1, 2, 3], [3, 5, 6]) == [3]


def test_no_common_elements():
    assert common_elements([1, 2], [3, 4]) == []


def test_same_lists():
    assert common_elements([1, 2, 3], [1, 2, 3]) == [1, 2, 3]