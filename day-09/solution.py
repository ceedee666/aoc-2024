import re
from pathlib import Path

import typer

app = typer.Typer()

FREE = -1


def read_input_file(input_file_path: str) -> str:
    p = Path(input_file_path)

    with p.open() as f:
        lines = f.readlines()

    return [line.strip() for line in lines][0]


def extract(data: str) -> list[int]:
    return [
        i // 2 if i % 2 == 0 else -1 for i, c in enumerate(data) for _ in range(int(c))
    ]


def extract_part_2(data: str) -> list[tuple[int, int]]:
    return [
        (i // 2, int(c)) if i % 2 == 0 else (FREE, int(c)) for i, c in enumerate(data)
    ]


def rearrange(disk: list[int]) -> list[int]:
    while FREE in disk:
        if disk[-1] == FREE:
            disk = disk[:-1]
        else:
            idx = disk.index(FREE)
            disk = disk[:idx] + [disk[-1]] + disk[idx + 1 : -1]
    return disk


def rearrange_part_2(disk: list[tuple[int, int]]) -> list[int]:
    for i in range(len(disk) - 1, -1, -1):
        for j in range(i):
            d1, s1 = disk[i]
            d2, s2 = disk[j]

            if d1 != FREE and d2 == FREE and s1 <= s2:
                disk[i] = (FREE, s1)
                disk[j] = (d1, s1)
                if s1 < s2:
                    disk = disk[: j + 1] + [(FREE, s2 - s1)] + disk[j + 1 :]
    return [d if d != -1 else 0 for d, s in disk for _ in range(s)]


def solve_part_1(data: str) -> int:
    disk = extract(data)
    disk = rearrange(disk)
    return sum([i * num for i, num in enumerate(disk)])


def solve_part_2(data: str) -> int:
    disk = extract_part_2(data)
    disk = rearrange_part_2(disk)
    return sum([i * num for i, num in enumerate(disk)])


@app.command()
def part_1(input_file: str = "input.txt"):
    data = read_input_file(input_file)
    print(f"The checksum is {solve_part_1(data)}")


@app.command()
def part_2(input_file: str = "input.txt"):
    data = read_input_file(input_file)
    print(f"The checksum is {solve_part_2(data)}")


if __name__ == "__main__":
    app()
