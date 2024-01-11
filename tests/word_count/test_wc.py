from coding_challenges.word_count.wc import calc_word_count


def test_calc_word_count():
    """
    Test the calc_word_count function.
    """
    assert calc_word_count("Hello World") == 3
    assert calc_word_count("Hello World!") == 2
    assert calc_word_count("Hello World!!") == 2
    assert calc_word_count("Hello World!!!") == 2
    # assert calc_word_count("Hello World!!!!") == 2
    # assert calc_word_count("Hello World!!!!!") == 2
    # assert calc_word_count("Hello World!!!!!!") == 2
    # assert calc_word_count("Hello World!!!!!!!") == 2
    # assert calc_word_count("Hello World!!!!!!!!") == 2
    # assert calc_word_count("Hello World!!!!!!!!!") == 2
    # assert calc_word_count("Hello World!!!!!!!!!!") == 2
    # assert calc_word_count("Hello World!!!!!!!!!!!") == 2
    # assert calc_word_count("Hello World!!!!!!!!!!!!") == 2
    # assert calc_word_count("Hello World!!!!!!!!!!!!!") == 2
    # assert calc_word_count("Hello World!!!!!!!!!!!!!!") == 2
    # assert calc_word_count("Hello World!!!!!!!!!!!!!!!") == 2
    # assert calc_word_count("Hello World!!!!!!!!!!!!!!!!") == 2
    # assert calc_word_count("Hello World!!!!!!!!!!!!!!!!!") == 2
    # assert calc_word_count("Hello World!!!!!!!!!!!!!!!!!!") == 2
    # assert calc_word_count("Hello World!!!!!!!!!!!!!!!!!!!") == 2
    # assert calc_word_count("Hello World!!!!!!!!!!!!!!!!!!!!") == 2
    # assert calc_word_count("Hello World!!!!!!!!!!!!!!!!!!!!!") == 2
    # assert calc_word_count("Hello World!!!!!!!!!!!!!!!!!!!!!!") == 2
    # assert calc_word_count("Hello World!!!!!!!!!!!!!!!!!!!!!!!") == 2
    # assert calc_word_count("Hello World!!!!!!!!!!!!!!!!!!!!!!!!") == 2
    # assert calc_word_count("Hello World!!!!!!!!!!!!!!!!!!!!!!!!!") == 2
    # assert calc_word_count("Hello World!!!!!!!!!!!!!!!!!!!!!!!!!!") == 2
    # assert calc_word_count("Hello World!!!!!!!!!!!!!!!!!!!!!!!!!!!") == 2
    # assert calc_word_count("Hello World!!!!!!!!!!!!!!!!!!!!!!!!!!!!") == 2
    # assert calc_word_count("Hello World!!!!!!!!!!!!!!!!!!!!!!!!!!!!!") == 2
    # assert calc_word_count("Hello World!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!") == 2
