import re

from operator import mul  # noqa: F401
from pathlib import Path

import typer

app = typer.Typer()


def read_input_file(input_file_path: str) -> list:
    p = Path(input_file_path)

    with p.open() as f:
        lines = f.readlines()

    return [line.strip() for line in lines]


def execute_mult(input: str) -> int:
    multiplications = re.findall(r"mul\(\d+,\d+\)", input)
    results = [eval(m) for m in multiplications]
    return sum(results)


def solve_part_1(input: list[str]) -> int:
    complete_input = "".join(input)
    return execute_mult(complete_input)


def solve_part_2(input: list[str]) -> int:
    complete_input = "".join(input)
    enabled = re.sub(r"don't\(\).*?do\(\)", "", complete_input)
    return execute_mult(enabled)


@app.command()
def part_1(input_file: str):
    input = read_input_file(input_file)
    print(f"The result is {solve_part_1(input)}")


@app.command()
def part_2(input_file: str):
    input = read_input_file(input_file)
    print(f"The result is {solve_part_2(input)}")


if __name__ == "__main__":
    app()
