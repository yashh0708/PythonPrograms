from mycode.vowels_consonants import count_vowels_consonants


def test_hello():
    assert count_vowels_consonants("Hello") == (2, 3)


def test_python():
    assert count_vowels_consonants("Python") == (1, 5)


def test_all_vowels():
    assert count_vowels_consonants("aeiou") == (5, 0)


def test_all_consonants():
    assert count_vowels_consonants("bcdf") == (0, 4)