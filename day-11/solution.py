from pathlib import Path
import typer
from functools import cache
from collections import defaultdict

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


def blink2(stones: dict[int, int]) -> dict[int, int]:
    new_stones = defaultdict(int)
    for s, c in stones.items():
        if s == 0:
            new_stones[1] += c
        elif len(str(s)) % 2 == 0:
            s_str = str(s)
            idx = len(s_str) // 2
            new_stones[int(s_str[idx:])] += c
            new_stones[int(s_str[:idx])] += c
        else:
            new_stones[s * 2024] += c
    return new_stones


def solve(data: list[str], blink_count: int = 25, recursive: bool = True) -> int:
    if recursive:
        stones = [int(n) for n in data[0].split()]
        return sum([blink(s, blink_count) for s in stones])
    else:
        stones = {int(n): 1 for n in data[0].split()}
        for _ in range(blink_count):
            stones = blink2(stones)
        return sum(stones.values())


@app.command()
def part_1(input_file: str = "input.txt", recursive: bool = True):
    data = read_input_file(input_file)
    print(
        f"There are {solve(data=data, recursive=recursive)} stones after blinking 25 times"
    )


@app.command()
def part_2(input_file: str = "input.txt", recursive: bool = True):
    data = read_input_file(input_file)
    print(f"There are {solve(data, 75, recursive)} stones after blinking 75 times")


if __name__ == "__main__":
    app()
