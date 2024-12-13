from pathlib import Path
import typer
import re
from itertools import product

app = typer.Typer()


def read_input_file(input_file_path: str) -> list[str]:
    p = Path(input_file_path)

    with p.open() as f:
        lines = f.readlines()

    return [line.strip() for line in lines]


def parse(
    data: list[str],
) -> list[tuple[tuple[int, int], tuple[int, int], tuple[int, int]]]:
    data = [d for d in data if d != ""]

    machines = []
    for i in range(0, len(data), 3):
        a = tuple(map(int, re.findall(r"\d+", data[i])))
        b = tuple(map(int, re.findall(r"\d+", data[i + 1])))
        p = tuple(map(int, re.findall(r"\d+", data[i + 2])))
        machines.append((a, b, p))
    return machines


def solve_eq(
    machine: tuple[tuple[int, int], tuple[int, int], tuple[int, int]],
) -> tuple[int, int]:
    a, b, p = machine
    x1, y1 = a
    x2, y2 = b
    c, d = p

    na = (d * x2 - c * y2) // (x2 * y1 - x1 * y2)
    nb = (d * x1 - c * y1) // (x1 * y2 - x2 * y1)

    if na * x1 + nb * x2 == c and na * y1 + nb * y2 == d:
        return na, nb
    else:
        return 0, 0


def solve(data: list[str], part: int = 1) -> int:
    machines = parse(data)
    if part == 1:
        solutions = [solve_eq(m) for m in machines]
    else:
        machines = [
            (a, b, (p[0] + 10000000000000, p[1] + 10000000000000))
            for a, b, p in machines
        ]
        solutions = [solve_eq(m) for m in machines]
    return sum(3 * a + b for a, b in solutions)


@app.command()
def part_1(input_file: str = "input.txt"):
    data = read_input_file(input_file)
    print(f"The fewest tokens to win all prices is {solve(data)}")


@app.command()
def part_2(input_file: str = "input.txt"):
    data = read_input_file(input_file)
    print(f"The fewest tokens to win all prices is {solve(data, 2)}")


if __name__ == "__main__":
    app()
