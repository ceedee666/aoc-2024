from collections import Counter
from pathlib import Path

import numpy as np
import typer

app = typer.Typer()


def read_input_file(input_file_path: str) -> list:
    p = Path(input_file_path)

    with p.open() as f:
        lines = f.readlines()

    return [line.strip() for line in lines]


def parse(data: list) -> tuple[list[int], list[int]]:
    left, right = zip(*map(lambda x: x.split(), data))
    left = sorted(map(int, left))
    right = sorted(map(int, right))
    return left, right


def solve_part_1(data: list) -> int:
    lists = parse(data)
    pairs = zip(lists[0], lists[1])
    diffs = map(lambda p: abs(p[1] - p[0]), pairs)
    return sum(diffs)


def solve_part_2(data: list) -> int:
    lists = parse(data)
    number_count = Counter(lists[1])
    similarity = [n * number_count[n] for n in lists[0] if n in number_count]
    return sum(similarity)


@app.command()
def part_1(input_file: str):
    data = read_input_file(input_file)
    print(f"The total distance of the lists is {solve_part_1(data)}")


@app.command()
def part_2(input_file: str):
    data = read_input_file(input_file)
    print(f"The similarity of the lists is {solve_part_2(data)}")


@app.command()
def numpy(input_file: str):
    A, B = np.transpose(np.loadtxt(input_file, np.integer))
    A, B = np.sort(A), np.sort(B)

    distance = np.sum(np.abs(A - B))
    print(f"The total distance of the lists is {distance}")

    similarity = sum(a * np.sum(B == a) for a in A)
    print(f"The similarity of the lists is {similarity}")


if __name__ == "__main__":
    app()
