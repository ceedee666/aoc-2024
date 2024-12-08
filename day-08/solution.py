from pathlib import Path
from collections import defaultdict
from itertools import permutations, chain

import typer

app = typer.Typer()


def read_input_file(input_file_path: str) -> list:
    p = Path(input_file_path)

    with p.open() as f:
        lines = f.readlines()

    return [line.strip() for line in lines]


def parse(data: list[str]) -> tuple[dict[str, set[complex]], set[complex]]:
    coords = {x + y * 1j: c for x, line in enumerate(data) for y, c in enumerate(line)}
    antennas = defaultdict(set)
    for p in coords:
        if coords[p] != ".":
            antennas[coords[p]].add(p)
    return antennas, set(coords.keys())


def antinodes(p: complex, q: complex, grid: set[complex], all: bool = False):
    d = q - p
    if all:
        nodes = [p + n * d for n in range(50)]
    else:
        nodes = [p + 2 * d]
    return [n for n in nodes if n in grid]


def solve(data: list[str], part2: bool = False) -> int:
    antennas, grid = parse(data)
    nodes = set(
        chain(
            *[
                antinodes(p, q, grid, part2)
                for a in antennas
                for p, q in permutations(antennas[a], 2)
            ]
        )
    )
    return len(nodes)


@app.command()
def part_1(input_file: str = "input.txt"):
    data = read_input_file(input_file)
    print(f"The number of antinnodes is {solve(data)}")


@app.command()
def part_2(input_file: str = "input.txt"):
    data = read_input_file(input_file)
    print(f"The number of antinnodes is {solve(data, True)}")


if __name__ == "__main__":
    app()
