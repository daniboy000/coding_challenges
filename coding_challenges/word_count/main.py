import typer

from coding_challenges.word_count.wc import get_file_size, get_number_of_lines

app = typer.Typer()


@app.command("c")
def call_get_file_size(file_path: str) -> None:
    """
    Print the file size in bytes

    Args:
        file_path: path to file

    Returns:
        None
    """
    try:
        print(get_file_size(file_path))
    except FileNotFoundError:
        print("File not found, check file path")


@app.command("l")
def call_get_number_of_lines(file_path: str) -> None:
    """
    Print the number of lines in a file

    Args:
        file_path: path to file

    Returns:
        None
    """
    try:
        print(get_number_of_lines(file_path))
    except FileNotFoundError:
        print("File not found, check file path")


if __name__ == "__main__":
    app()
