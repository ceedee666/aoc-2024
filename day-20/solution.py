from heapq import heappop, heappush
from itertools import combinations
from pathlib import Path

import typer

app = typer.Typer()

D = [1, -1, 1j, -1j]


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
) -> dict[complex, int]:
    pq = []
    heappush(pq, (0, start))

    dists = {}

    while pq:
        cost, current = heappop(pq)
        current = complex(current)
        if current in dists and dists[current] <= cost:
            continue

        dists[current] = cost

        for direction in D:
            neighbor = current + direction

            if neighbor in maze and maze[neighbor] != "#":
                heappush(pq, (cost + 1, str(neighbor)))
    return dists


def manhatten_dist(a: complex, b: complex) -> int:
    return int(abs(a.real - b.real) + abs(a.imag - b.imag))


def possible_cheats(
    dists: dict[complex, int], minimal_saves: int, cheat_time: int
) -> int:
    ret = 0
    for a, b in combinations(dists, 2):
        cheat_cost = manhatten_dist(a, b)
        initial_cost = dists[b] - dists[a]
        if cheat_cost <= cheat_time and (initial_cost - cheat_cost) >= minimal_saves:
            ret += 1
    return ret


def solve(data: list[str], minimal_saves: int = 100, cheat_time=2) -> int:
    start, end, maze = parse(data)
    dists = shortest_path(start, end, maze)
    return possible_cheats(dists, minimal_saves, cheat_time)


@app.command()
def part_1(input_file: str = "input.txt"):
    data = read_input_file(input_file)
    print(f"{solve(data)} cheats save at least 100 picoseconds.")


@app.command()
def part_2(input_file: str = "input.txt"):
    data = read_input_file(input_file)
    print(f"{solve(data, cheat_time=20)} cheats save at least 100 picoseconds.")


if __name__ == "__main__":
    app()
