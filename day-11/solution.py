from pathlib import Path
import typer
from itertools import chain
from functools import cache

app = typer.Typer()


def read_input_file(input_file_path: str) -> list[str]:
    p = Path(input_file_path)

    with p.open() as f:
        lines = f.readlines()

    return [line.strip() for line in lines]


@cache
def blink(stone: int, iterations: int) -> int:
    if iterations == 0:
        return 1
    if stone == 0:
        return blink(1, iterations - 1)
    if len(str(stone)) % 2 == 0:
        s = str(stone)
        idx = len(s) // 2
        return blink(int(s[:idx]), iterations - 1) + blink(int(s[idx:]), iterations - 1)
    return blink(stone * 2024, iterations - 1)


def solve(data: list[str], blink_count: int = 25) -> int:
    stones = [int(n) for n in data[0].split()]

    return sum([blink(s, blink_count) for s in stones])


@app.command()
def part_1(input_file: str = "input.txt"):
    data = read_input_file(input_file)
    print(f"There are {solve(data)} stones after blinking 25 times")


@app.command()
def part_2(input_file: str = "input.txt"):
    data = read_input_file(input_file)
    print(f"There are {solve(data, 75)} stones after blinking 75 times")


if __name__ == "__main__":
    app()
