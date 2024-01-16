from coding_challenges.word_count.wc import calc_word_count, get_file_size


def test_calc_word_count():
    """
    Test the calc_word_count function.
    """
    assert calc_word_count("Hello World") == 2


def test_get_file_size():
    """
    Test the get_file_size function.
    """
    assert get_file_size("tests/test.txt") == 342190
