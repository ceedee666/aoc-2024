from heapq import heappop, heappush
from pathlib import Path

import typer

app = typer.Typer()


def read_input_file(input_file_path: str) -> list[str]:
    p = Path(input_file_path)

    with p.open() as f:
        lines = f.readlines()

    return [line.strip() for line in lines]


def parse(
    data: list[str], width: int, height: int, steps: int
) -> tuple[dict[complex, str], list[complex]]:
    grid = {(i + 1j * j): "" for j in range(height) for i in range(width)}
    corrupted = [d.split(",") for d in data]
    corrupted = [(int(c[0]) + 1j * int(c[1])) for c in corrupted]
    for i in range(steps):
        grid[corrupted[i]] = "#"
    return grid, corrupted


def shortest_path(
    grid: dict[complex, str], start: complex = 0 + 1j * 0, end: complex = 70 + 1j * 70
) -> dict[complex, int]:
    directions = [1, -1, 1j, -1j]

    pq = []
    heappush(pq, (0, start))

    dists = {}

    while pq:
        cost, current = heappop(pq)
        current = complex(current)
        if current in dists and dists[current] <= cost:
            continue

        dists[current] = cost

        for direction in directions:
            neighbor = current + direction

            if neighbor in grid and grid[neighbor] != "#":
                heappush(pq, (cost + 1, str(neighbor)))

    return dists


def solve(
    data: list[str],
    width: int = 71,
    height: int = 71,
    steps: int = 1024,
    end: complex = 70 + 1j * 70,
) -> int:
    grid, _ = parse(data, width, height, steps)
    dists = shortest_path(grid)
    return dists[end] if end in dists else -1


@app.command()
def part_1(input_file: str = "input.txt"):
    data = read_input_file(input_file)
    print(f"The output of the program is {solve(data)}")


@app.command()
def part_2(input_file: str = "input.txt"):
    data = read_input_file(input_file)
    _, corruptes = parse(data, 0, 0, 0)

    path_blocked = False
    i = 1024
    while not path_blocked:
        dist = solve(data, steps=i)
        if dist == -1:
            path_blocked = True
        else:
            i += 1

    pos = corruptes[i - 1]

    print(f"The fist coordinate blocking the path is {int(pos.real)},{int(pos.imag)})")


if __name__ == "__main__":
    app()
