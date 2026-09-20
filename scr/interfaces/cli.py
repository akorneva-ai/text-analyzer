import click

from .api import analyze_text


@click.group()
def cli():
    """CLI для анализа текста."""
    pass


@cli.command()
@click.option("--text", type=str, help="Текст для анализа")
@click.option("--file", type=click.Path(exists=True), help="Путь к файлу с текстом")
@click.option(
    "--batch-file",
    type=click.Path(exists=True),
    help="Путь к файлу с несколькими текстами"
)
def analyze(text, file, batch_file):
    """Анализирует текст, файл или несколько текстов."""

    # Проверяем, что указан ровно один режим
    options = [text is not None, file is not None, batch_file is not None]

    if sum(options) == 0:
        raise click.UsageError(
            "Нужно указать --text, --file или --batch-file"
        )

    if sum(options) > 1:
        raise click.UsageError(
            "Можно использовать только один из: --text, --file, --batch-file"
        )

    # -------------------------
    # Анализ одного текста
    # -------------------------
    if text is not None:
        result = analyze_text(text)

        click.echo(f"Text: {result['text']}")
        click.echo(f"Polarity: {result['polarity']}")
        click.echo(f"Subjectivity: {result['subjectivity']}")

    # -------------------------
    # Анализ одного файла
    # -------------------------
    elif file is not None:
        with open(file, "r", encoding="utf-8") as f:
            text = f.read()

        result = analyze_text(text)

        click.echo(f"Text: {result['text']}")
        click.echo(f"Polarity: {result['polarity']}")
        click.echo(f"Subjectivity: {result['subjectivity']}")

    # -------------------------
    # Анализ нескольких текстов
    # -------------------------
    elif batch_file is not None:
        with open(batch_file, "r", encoding="utf-8") as f:
            texts = [line.strip() for line in f if line.strip()]

        for i, text in enumerate(texts, start=1):
            result = analyze_text(text)

            click.echo(f"\n--- Text {i} ---")
            click.echo(f"Text: {result['text']}")
            click.echo(f"Polarity: {result['polarity']}")
            click.echo(f"Subjectivity: {result['subjectivity']}")


if __name__ == "__main__":
    cli()