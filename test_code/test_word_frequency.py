from mycode.word_frequency import word_frequency


def test_word_frequency():
    assert word_frequency("hello world hello") == {
        "hello": 2,
        "world": 1
    }


def test_repeated_words():
    assert word_frequency("python python python") == {
        "python": 3
    }


def test_different_words():
    assert word_frequency("I love Python") == {
        "i": 1,
        "love": 1,
        "python": 1
    }


def test_empty_sentence():
    assert word_frequency("") == {}