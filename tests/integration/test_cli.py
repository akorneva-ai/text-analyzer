import pytest
from click.testing import CliRunner
from scr.interfaces.cli import cli


def test_cli_no_options_error():
    runner = CliRunner()
    result = runner.invoke(cli, ["analyze"])

    assert result.exit_code != 0
    assert "Нужно указать --text, --file или --batch-file" in result.output


def test_cli_multiple_options_error(tmp_path):
    runner = CliRunner()
    # Создаем временный файл, который физически существует на компьютере
    fake_file = tmp_path / "exist.txt"
    fake_file.write_text("content")

    result = runner.invoke(cli, ["analyze", "--text", "Hello", "--file", str(fake_file)])

    assert result.exit_code != 0
    assert "Можно использовать только один из" in result.output


def test_cli_analyze_text_success():
    runner = CliRunner()
    result = runner.invoke(cli, ["analyze", "--text", "This is a wonderful day!"])

    assert result.exit_code == 0
    assert "Polarity:" in result.output
    assert "Subjectivity:" in result.output


def test_cli_analyze_file_success(tmp_path):
    runner = CliRunner()
    test_file = tmp_path / "single_text.txt"
    test_file.write_text("Python coding is beautiful.", encoding="utf-8")

    result = runner.invoke(cli, ["analyze", "--file", str(test_file)])

    assert result.exit_code == 0
    assert "Text: Python coding is beautiful." in result.output


def test_cli_analyze_batch_file_success(tmp_path):
    runner = CliRunner()
    test_file = tmp_path / "batch.txt"
    test_file.write_text("First text line.\nSecond text line.\n", encoding="utf-8")

    result = runner.invoke(cli, ["analyze", "--batch-file", str(test_file)])

    assert result.exit_code == 0
    assert "--- Text 1 ---" in result.output
    assert "--- Text 2 ---" in result.output
