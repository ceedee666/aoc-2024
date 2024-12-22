from pathlib import Path
from itertools import pairwise
from collections import defaultdict

import typer

app = typer.Typer()


def read_input_file(input_file_path: str) -> list[str]:
    p = Path(input_file_path)

    with p.open() as f:
        lines = f.readlines()

    return [line.strip() for line in lines]


def secrets(n: int, steps: int) -> list[int]:
    a = n
    seq = [n]
    for _ in range(steps):
        b = a * 64
        a = b ^ a
        a %= 16777216

        b = a // 32
        a = b ^ a
        a %= 16777216

        b = a * 2048
        a = b ^ a
        a %= 16777216

        seq += [a]
    return seq


def solve(data: list[str], steps: int = 2000, part: int = 1) -> int:
    numbers = list(map(int, data))
    if part == 1:
        return sum([secrets(n, steps)[-1] for n in numbers])
    else:
        bananas = defaultdict(int)
        for n in numbers:
            nums = secrets(n, steps)
            prices = [n % 10 for n in nums]
            diffs = [b - a for a, b in pairwise(prices)]

            seen = set()
            for i in range(len(nums) - 4):
                p = tuple(diffs[i : i + 4])
                if p not in seen:
                    seen.add(p)
                    bananas[p] += prices[i + 4]
        return max(bananas.values())


@app.command()
def part_1(input_file: str = "input.txt"):
    data = read_input_file(input_file)
    print(f"The sum of the 2000th secret number is {solve(data)}")


@app.command()
def part_2(input_file: str = "input.txt"):
    data = read_input_file(input_file)
    print(f"The maximum number of bananas is {solve(data,part = 2)}")


if __name__ == "__main__":
    app()
