from pathlib import Path

import typer

app = typer.Typer()

MOVEMENTS = {">": 1 + 0j, "<": -1 + 0j, "v": 0 + 1j, "^": 0 - 1j}


def read_input_file(input_file_path: str) -> list[str]:
    p = Path(input_file_path)

    with p.open() as f:
        lines = f.readlines()

    return [line.strip() for line in lines]


def parse(
    data: list[str], part: int = 1
) -> tuple[complex, dict[complex, str], list[complex]]:
    idx = data.index("")
    grid_data = data[:idx]
    movements_data = data[idx + 1 :]

    if part == 2:
        grid_data = [
            line.replace("#", "##")
            .replace("O", "[]")
            .replace(".", "..")
            .replace("@", "@.")
            for line in grid_data
        ]

    grid = dict()
    robot = 0 + 0

    grid = {
        i + 1j * j: c for j, line in enumerate(grid_data) for i, c in enumerate(line)
    }

    for pos, c in grid.items():
        if c == "@":
            robot = pos
            grid[pos] = "."

    movements = [MOVEMENTS[c] for c in "".join(movements_data)]

    return robot, grid, movements


def can_move(pos: complex, grid: dict[complex, str], d: complex) -> bool:
    if grid[pos] == "#":
        return False
    if grid[pos] == ".":
        return True
    if int(d.real) == 0:
        if grid[pos] == "[":
            return can_move(pos + d, grid, d) and can_move(pos + 1 + d, grid, d)
        if grid[pos] == "]":
            return can_move(pos + d, grid, d) and can_move(pos - 1 + d, grid, d)
        if grid[pos] == "O":
            return can_move(pos + d, grid, d)
    else:
        return can_move(pos + d, grid, d)
    return False


def move(pos: complex, grid: dict[complex, str], d: complex) -> dict[complex, str]:
    new_grid = grid.copy()
    if new_grid[pos] in "[]O":
        if int(d.real) == 0:
            if new_grid[pos] == "[":
                new_grid = move(pos + d, new_grid, d)
                new_grid = move(pos + d + 1, new_grid, d)

                new_grid[pos + d] = new_grid[pos]
                new_grid[pos] = "."
                new_grid[pos + d + 1] = new_grid[pos + 1]
                new_grid[pos + 1] = "."

            if new_grid[pos] == "]":
                new_grid = move(pos + d, new_grid, d)
                new_grid = move(pos + d - 1, new_grid, d)

                new_grid[pos + d] = new_grid[pos]
                new_grid[pos] = "."
                new_grid[pos + d - 1] = new_grid[pos - 1]
                new_grid[pos - 1] = "."

            if new_grid[pos] == "O":
                new_grid = move(pos + d, new_grid, d)
                new_grid[pos + d] = new_grid[pos]
                new_grid[pos] = "."
        else:
            new_grid = move(pos + d, new_grid, d)
            new_grid[pos + d] = new_grid[pos]
            new_grid[pos] = "."
    return new_grid


def execute_moves(
    robot: complex, grid: dict[complex, str], movements: list[complex], part: int = 1
) -> tuple[complex, dict[complex, str]]:
    for d in movements:
        if can_move(robot + d, grid, d):
            grid = move(robot + d, grid, d)
            robot += d
    return robot, grid


def print_grid(robot: complex, grid: dict[complex, str]):
    max_x = int(max(p.real for p in grid.keys()))
    max_y = int(max(p.imag for p in grid.keys()))

    grid_str = ""
    for y in range(max_y + 1):
        for x in range(max_x + 1):
            pos = x + 1j * y
            if pos == robot:
                grid_str += "@"
            else:
                grid_str += grid[x + 1j * y]
        grid_str += "\n"

    print(grid_str)


def solve(data: list[str], part: int = 1, show_grid: bool = False) -> int:
    robot, grid, movements = parse(data, part)

    if show_grid:
        print("Initial grid:")
        print_grid(robot, grid)

    robot, grid = execute_moves(robot, grid, movements, part)

    if show_grid:
        print("Grid after all movements:")
        print_grid(robot, grid)

    boxes = {p: c for p, c in grid.items() if c in "O["}
    return sum(int(p.real) + 100 * int(p.imag) for p in boxes)


@app.command()
def part_1(input_file: str = "input.txt", show_grid: bool = False):
    data = read_input_file(input_file)
    print(f"The sum of the GPS coordinates is {solve(data, 1, show_grid)}")


@app.command()
def part_2(input_file: str = "input.txt", show_grid: bool = False):
    data = read_input_file(input_file)
    print(f"The sum of the GPS coordinates is {solve(data,2, show_grid)}")


if __name__ == "__main__":
    app()
