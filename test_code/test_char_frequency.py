from mycode.char_frequency import char_frequency


def test_character_frequency():
    assert char_frequency("hello") == {
        "h": 1,
        "e": 1,
        "l": 2,
        "o": 1
    }


def test_repeated_character():
    assert char_frequency("aaa") == {
        "a": 3
    }


def test_unique_characters():
    assert char_frequency("abc") == {
        "a": 1,
        "b": 1,
        "c": 1
    }


def test_empty_string():
    assert char_frequency("") == {}