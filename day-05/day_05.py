import re
from pathlib import Path

import typer

app = typer.Typer()


def read_input_file(input_file_path: str) -> list:
    p = Path(input_file_path)

    with p.open() as f:
        lines = f.readlines()

    return [line.strip() for line in lines]


@app.command()
def part_1(input_file: str):
    data = read_input_file(input_file)
    print(f"The result is....")


if __name__ == "__main__":
    app()
