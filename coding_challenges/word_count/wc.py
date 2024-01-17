import os


def calc_word_count(text: str) -> int:
    """
    Calculate the number of words in a text.
    """
    return len(text.split())


def get_number_of_lines(file_path: str) -> int:
    """
    Calculate the number of lines in a text file.

    Args:
        file_path: path to file

    Returns:
        int: number of lines in file
    """
    with open(file_path, "r") as f:
        return len(f.readlines())


def get_file_size(file_path: str) -> int:
    """
    Returns the file size in bytes.

    Args:
        file_path: path to file

    Returns:
        int: file size in bytes
    """
    return os.path.getsize(file_path)
