from typer.testing import CliRunner

from coding_challenges.word_count.main import app, call_get_file_size, call_get_number_of_lines

runner = CliRunner()


def test_app(mocker):
    expected_file_size = 1000
    mocker.patch("coding_challenges.word_count.main.get_file_size", return_value=expected_file_size)

    result = runner.invoke(app, ["c", "test_file"])

    assert result.exit_code == 0
    assert str(expected_file_size) in result.stdout


def test_call_get_file_size(mocker, capfd):
    expected_file_size = 1000
    mocker.patch("coding_challenges.word_count.main.get_file_size", return_value=expected_file_size)

    call_get_file_size(file_path="test_file")

    out, _ = capfd.readouterr()
    assert out == f"{expected_file_size}\n"


def test_call_get_file_size_file_not_found(mocker, capfd):
    mocker.patch("coding_challenges.word_count.main.get_file_size", side_effect=FileNotFoundError)

    call_get_file_size(file_path="test_file")

    out, _ = capfd.readouterr()
    assert out == "File not found, check file path\n"


def test_call_get_number_of_lines(mocker, capfd):
    expected_number_of_lines = 200
    mocker.patch(
        "coding_challenges.word_count.main.get_number_of_lines",
        return_value=expected_number_of_lines,
    )

    call_get_number_of_lines(file_path="test_file")

    out, _ = capfd.readouterr()
    assert out == f"{expected_number_of_lines}\n"


def test_call_get_number_of_lines_file_not_found(mocker, capfd):
    mocker.patch(
        "coding_challenges.word_count.main.get_number_of_lines", side_effect=FileNotFoundError
    )

    call_get_number_of_lines(file_path="test_file")

    out, _ = capfd.readouterr()
    assert out == "File not found, check file path\n"
