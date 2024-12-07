import re
from pathlib import Path

import typer

app = typer.Typer()


def read_input_file(input_file_path: str) -> list:
    p = Path(input_file_path)

    with p.open() as f:
        lines = f.readlines()

    return [line.strip() for line in lines]


def is_possible_equation(equation: tuple[int, list[int]], concat_allowed: bool) -> bool:
    r, ns = equation
    results = [ns[0]]
    for n in ns[1:]:
        if concat_allowed:
            results = (
                [n * r for r in results]
                + [n + r for r in results]
                + [int(str(r) + str(n)) for r in results]
                + [int(str(n) + str(r)) for r in results]
            )
        else:
            results = [n * r for r in results] + [n + r for r in results]
    return r in results


def solve(data: list[str], concat_allowed: bool = False) -> int:
    equations = [
        (int(line.split(": ")[0]), list(map(int, line.split(": ")[1].split(" "))))
        for line in data
    ]
    possible_eqs = list(
        filter(lambda e: is_possible_equation(e, concat_allowed), equations)
    )
    return sum([r for r, ns in possible_eqs])


@app.command()
def part_1(input_file: str = "input.txt"):
    data = read_input_file(input_file)
    print(f"The calibration result is {solve(data)}")


@app.command()
def part_2(input_file: str = "input.txt"):
    data = read_input_file(input_file)
    print(f"The calibration result is {solve(data, True)}")


if __name__ == "__main__":
    app()
