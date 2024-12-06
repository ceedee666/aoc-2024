import re

from operator import mul  # noqa: F401
from pathlib import Path

import typer

app = typer.Typer()


def read_input_file(input_file_path: str) -> str:
    p = Path(input_file_path)

    with p.open() as f:
        lines = f.readlines()

    return "".join([line.strip() for line in lines])


def execute_mult(input: str) -> int:
    multiplications = re.findall(r"mul\(\d+,\d+\)", input)
    results = [eval(m) for m in multiplications]
    return sum(results)


def solve_part_1(input: str) -> int:
    return execute_mult(input)


def solve_part_2(input: str) -> int:
    enabled = re.sub(r"don't\(\).*?do\(\)", "", input)
    return execute_mult(enabled)


def solve_part_2_differntly(input: str) -> int:
    result_all = solve_part_1(input)
    disabled = "".join(re.findall(r"don't\(\).*?do\(\)", input))
    result_disabled = solve_part_1(disabled)
    return result_all - result_disabled


@app.command()
def part_1(input_file: str):
    input = read_input_file(input_file)
    print(f"The result is {solve_part_1(input)}")


@app.command()
def part_2(input_file: str):
    input = read_input_file(input_file)
    print(f"The result is {solve_part_2(input)}")


@app.command()
def part_2a(input_file: str):
    input = read_input_file(input_file)
    print(f"The result is {solve_part_2(input)}")


if __name__ == "__main__":
    app()
