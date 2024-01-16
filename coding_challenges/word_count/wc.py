import os


def calc_word_count(text: str) -> int:
    """
    Calculate the number of words in a text.
    """
    return len(text.split())


def get_file_size(file_path: str) -> int:
    """
    Get the size of a file in bytes.
    """
    return os.path.getsize(file_path)
