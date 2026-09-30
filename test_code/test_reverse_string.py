from mycode.reverse_string import reverse_string


def test_reverse_hello():
    assert reverse_string("hello") == "olleh"


def test_reverse_python():
    assert reverse_string("python") == "nohtyp"


def test_reverse_single_character():
    assert reverse_string("a") == "a"


def test_reverse_empty_string():
    assert reverse_string("") == ""