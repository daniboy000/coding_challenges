from coding_challenges.word_count.wc import (
    calc_word_count,
    get_file_size,
    get_number_of_lines,
)

FILE_PATH = "tests/test.txt"


def test_calc_word_count():
    """
    Test the calc_word_count function.
    """
    assert calc_word_count("Hello World") == 2


def test_get_file_size():
    """
    Test the get_file_size function.
    """
    assert get_file_size(FILE_PATH) == 342190


def test_get_number_of_lines():
    assert get_number_of_lines(FILE_PATH) == 7145
