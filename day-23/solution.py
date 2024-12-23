from pathlib import Path
from collections import defaultdict
from itertools import combinations
import typer

app = typer.Typer()


def read_input_file(input_file_path: str) -> list[str]:
    p = Path(input_file_path)

    with p.open() as f:
        lines = f.readlines()

    return [line.strip() for line in lines]


def all_neighbors(lines: list[str]) -> dict[str, set[str]]:
    n = defaultdict(set)
    pairs = [line.split("-") for line in lines]
    for k, v in pairs:
        n[k].add(v)
        n[v].add(k)
    return n


def solve_1(data: list[str]) -> int:
    neighbors = all_neighbors(data)
    groups = [
        (a, b, c)
        for a, b, c in combinations(neighbors, 3)
        if a in neighbors[b] and b in neighbors[c] and c in neighbors[a]
    ]
    groups = [(a, b, c) for a, b, c in groups if "t" in a[0] + b[0] + c[0]]
    return len(groups)


def solve_2(data: list[str]) -> str:
    neighbors = all_neighbors(data)
    networks = [{n} for n in neighbors]

    for net in networks:
        for computer in neighbors:
            if all(c in neighbors[computer] for c in net):
                net |= {computer}

    largest = sorted(networks, key=len)[-1]
    return ",".join(sorted(largest))


@app.command()
def part_1(input_file: str = "input.txt"):
    data = read_input_file(input_file)
    print(f"{solve_1(data)} sets contain a computer with letter t")


@app.command()
def part_2(input_file: str = "input.txt"):
    data = read_input_file(input_file)
    print(f"The password is: {solve_2(data)}")


if __name__ == "__main__":
    app()
