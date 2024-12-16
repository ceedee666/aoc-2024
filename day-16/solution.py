import heapq as h
from collections import defaultdict
from pathlib import Path

import typer

app = typer.Typer()

D = [1, 1j, -1j]


def read_input_file(input_file_path: str) -> list[str]:
    p = Path(input_file_path)

    with p.open() as f:
        lines = f.readlines()

    return [line.strip() for line in lines]


def parse(data: list[str]) -> tuple[complex, complex, dict[complex, str]]:
    maze = dict()
    start, end = 0 + 0j, 0 + 0j
    for j, line in enumerate(data):
        for i, c in enumerate(line):
            if c != "#":
                pos = i + 1j * j
                maze[pos] = c
                if c == "S":
                    maze[pos] = "."
                    start = pos
                if c == "E":
                    maze[pos] = "."
                    end = pos
    return start, end, maze


def shortest_path(
    start: complex, end: complex, maze: dict[complex, str]
) -> tuple[int, list[complex]]:
    visited = []
    costs = defaultdict(lambda: int(1e10))
    minimal_costs = int(1e10)

    hq = [(0, str(start), str(1), [str(start)])]
    while hq:
        cost, pos, dir, path = h.heappop(hq)
        pos = complex(pos)
        dir = complex(dir)

        if cost > costs[(pos, dir)]:
            continue
        else:
            costs[(pos, dir)] = cost

        if pos == end and cost <= minimal_costs:
            visited += path
            minimal_costs = cost

        for d in D:
            next_pos = pos + dir * d
            next_dir = dir * d
            if next_pos in maze:
                next_costs = cost + 1
                if int(d.imag) != 0:
                    next_costs += 1000
                h.heappush(
                    hq,
                    (next_costs, str(next_pos), str(next_dir), path + [str(next_pos)]),
                )
    return minimal_costs, visited


def solve(data: list[str], part: int = 1) -> int:
    start, end, maze = parse(data)
    costs, visited = shortest_path(start, end, maze)
    if part == 1:
        return costs
    else:
        return len(set(visited))


@app.command()
def part_1(input_file: str = "input.txt"):
    data = read_input_file(input_file)
    print(f"The lowest possible score is {solve(data, 1)}")


@app.command()
def part_2(input_file: str = "input.txt"):
    data = read_input_file(input_file)
    print(f"{solve(data, 2)} tiles are part of one of the best paths.")


if __name__ == "__main__":
    app()
