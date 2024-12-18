from heapq import heappop, heappush
from pathlib import Path

import typer

app = typer.Typer()


def read_input_file(input_file_path: str) -> list[str]:
    p = Path(input_file_path)

    with p.open() as f:
        lines = f.readlines()

    return [line.strip() for line in lines]


def parse(data: list[str]) -> list[complex]:
    bytes = [d.split(",") for d in data]
    bytes = [(int(c[0]) + 1j * int(c[1])) for c in bytes]
    return bytes


def initialize_memory(width: int, height: int) -> dict[complex, str]:
    return {(i + 1j * j): "" for j in range(height) for i in range(width)}


def corrupt_memory(
    memory: dict[complex, str], bytes: list[complex], num_of_bytes: int
) -> dict[complex, str]:
    corrupted_memory = memory.copy()

    for i in range(num_of_bytes):
        corrupted_memory[bytes[i]] = "#"

    return corrupted_memory


def shortest_paths(
    grid: dict[complex, str], end: complex = 70 + 1j * 70
) -> dict[complex, int]:
    directions = [1, -1, 1j, -1j]
    start = 0 + 1j * 0

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
    bytes = parse(data)
    memory = initialize_memory(width, height)
    memory = corrupt_memory(memory, bytes, steps)
    dists = shortest_paths(memory, end)
    return dists[end] if end in dists else -1


def solve_2(
    data: list[str],
    width: int = 71,
    height: int = 71,
    steps: int = 1024,
    end: complex = 70 + 1j * 70,
) -> tuple[int, int]:
    bytes = parse(data)
    i = steps
    path_blocked = False

    while not path_blocked:
        memory = initialize_memory(width, height)
        memory = corrupt_memory(memory, bytes, i)
        dists = shortest_paths(memory, end)

        if end not in dists:
            path_blocked = True
        else:
            i += 1

    pos = bytes[i - 1]
    return int(pos.real), int(pos.imag)


@app.command()
def part_1(input_file: str = "input.txt"):
    data = read_input_file(input_file)
    print(f"The output of the program is {solve(data)}")


@app.command()
def part_2(input_file: str = "input.txt"):
    data = read_input_file(input_file)
    print(f"The fist coordinate blocking the path is {solve_2(data)}")


if __name__ == "__main__":
    app()
