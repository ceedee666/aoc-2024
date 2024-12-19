from functools import cache
from pathlib import Path

import typer

app = typer.Typer()


def read_input_file(input_file_path: str) -> list[str]:
    p = Path(input_file_path)

    with p.open() as f:
        lines = f.readlines()

    return [line.strip() for line in lines]


def parse(data: list[str]) -> tuple[tuple[str, ...], list[str]]:
    towels = tuple(data[0].split(", "))
    designs = data[2:]
    return towels, designs


# Solution for the first part I didn't use in the end...
def check_pattern(design: str, towels: tuple[str, ...]) -> bool:
    n = len(design)
    dp = [False] * (n + 1)
    dp[0] = True

    for i in range(1, n + 1):
        for t in towels:
            t_len = len(t)
            if i >= t_len and design[i - t_len : i] == t and dp[i - t_len]:
                dp[i] = True
                break
    return dp[n]


@cache
def count_possibilities(design: str, towels: tuple[str, ...]) -> int:
    if design == "":
        return 1

    possibilities = 0
    for t in towels:
        if design.startswith(t):
            possibilities += count_possibilities(design[len(t) :], towels)

    return possibilities


def solve(data: list[str], part: int = 1) -> int:
    towels, designs = parse(data)
    if part == 1:
        posibilities = [count_possibilities(p, towels) for p in designs]
        return len([p for p in posibilities if p > 0])
    else:
        return sum([count_possibilities(p, towels) for p in designs])


@app.command()
def part_1(input_file: str = "input.txt"):
    data = read_input_file(input_file)
    print(f"{solve(data)} designs are possible.")


@app.command()
def part_2(input_file: str = "input.txt"):
    data = read_input_file(input_file)
    print(f"There are {solve(data,2)} different ways to create the possible designs.")


if __name__ == "__main__":
    app()
