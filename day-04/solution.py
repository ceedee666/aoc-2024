from collections import defaultdict
from pathlib import Path

import typer

app = typer.Typer()

DELTAS = [-1, 0, 1]


def read_input_file(input_file_path: str) -> list:
    p = Path(input_file_path)

    with p.open() as f:
        lines = f.readlines()

    return [line.strip() for line in lines]


def possible_word_indices(x: int, y: int) -> list[list[tuple[int, int]]]:
    word_indices = [
        [(x + dx * n, y + dy * n) for n in range(4)] for dx in DELTAS for dy in DELTAS
    ]
    return word_indices


def possible_x_mas_indices(x: int, y: int) -> list[list[tuple[int, int]]]:
    x_mas_indices = []

    x_mas_indices.append([(x - 1, y - 1), (x, y), (x + 1, y + 1)])
    x_mas_indices.append([(x - 1, y + 1), (x, y), (x + 1, y - 1)])
    x_mas_indices.append([(x + 1, y + 1), (x, y), (x - 1, y - 1)])
    x_mas_indices.append([(x + 1, y - 1), (x, y), (x - 1, y + 1)])

    return x_mas_indices


def build_char_map(data: list[str]) -> dict[tuple[int, int], str]:
    cm = defaultdict(lambda: "")
    for i, _ in enumerate(data):
        for j, c in enumerate(data[i]):
            cm[(i, j)] = c
    return cm


def count_xmas(i: int, j: int, char_map: dict[tuple[int, int], str]) -> int:
    word_indices = possible_word_indices(i, j)

    words = ["".join([char_map[x, y] for x, y in w]) for w in word_indices]
    word_is_xmas = [w == "XMAS" for w in words]
    return sum(word_is_xmas)


def is_x_mas_centers(i: int, j: int, char_map: dict[tuple[int, int], str]) -> bool:
    x_mas_indices = possible_x_mas_indices(i, j)

    words = ["".join([char_map[x, y] for x, y in w]) for w in x_mas_indices]
    word_is_mas = [w == "MAS" for w in words]
    return sum(word_is_mas) == 2


def solve_part_1(data: list[str]) -> int:
    size_x, size_y = len(data[0]), len(data)
    char_map = build_char_map(data)
    xmas_count = [
        count_xmas(i, j, char_map) for i in range(size_x) for j in range(size_y)
    ]
    return sum(xmas_count)


def solve_part_2(data: list[str]) -> int:
    size_x, size_y = len(data[0]), len(data)
    char_map = build_char_map(data)
    x_mas_count = [
        is_x_mas_centers(i, j, char_map) for i in range(size_x) for j in range(size_y)
    ]
    return sum(x_mas_count)


@app.command()
def part_1(input_file: str):
    data = read_input_file(input_file)
    print(f"XMAS appears {solve_part_1(data)} times.")


@app.command()
def part_2(input_file: str):
    data = read_input_file(input_file)
    print(f"X-MAS appears {solve_part_2(data)} times.")


if __name__ == "__main__":
    app()
