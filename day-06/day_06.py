import re
from pathlib import Path

import typer

app = typer.Typer()


def read_input_file(input_file_path: str) -> list[str]:
    p = Path(input_file_path)

    with p.open() as f:
        lines = f.readlines()

    return [line.strip() for line in lines]


def parse(
    data: list[str],
) -> tuple[tuple[complex, complex], dict[complex, str]]:
    grid = {x + 1j * y: c for y, line in enumerate(data) for x, c in enumerate(line)}
    start = [p for p in grid if grid[p] == "^"][0]
    guard = (start, -1j)
    return guard, grid


def next_guard(
    current: tuple[complex, complex], grid: dict[complex, str]
) -> tuple[complex, complex]:
    pos, dir = current
    if grid[pos + dir] == "#":
        return pos, dir * 1j
    else:
        return pos + dir, dir


def track_guard(
    start: tuple[complex, complex], grid: dict[complex, str]
) -> tuple[set[tuple[complex, complex]], bool]:
    current = start
    visited = {current}

    while True:
        pos, dir = current

        if pos + dir not in grid:
            return visited, False
        else:
            next = next_guard(current, grid)
            if next in visited:
                return visited, True
            else:
                visited |= {next}
                current = next


def solve_part_1(data: list[str]) -> int:
    start, grid = parse(data)
    visited, _ = track_guard(start, grid)
    return len({pos for pos, _ in visited})


def solve_part_2(data: list[str]) -> int:
    start, grid = parse(data)
    visited, _ = track_guard(start, grid)
    possible = {p for p, _ in visited if p != start[0]}
    possible_grids = [{k: grid[k] if k != p else "#" for k in grid} for p in possible]
    all_paths = [track_guard(start, g) for g in possible_grids]
    loops = [p for p in all_paths if p[1]]
    return len(loops)


@app.command()
def part_1(input_file: str):
    data = read_input_file(input_file)
    print(f"The guard visits {solve_part_1(data)} positions.")


@app.command()
def part_2(input_file: str):
    data = read_input_file(input_file)
    print(f"The are {solve_part_2(data)} positions to force the guard in a loop.")


if __name__ == "__main__":
    app()
