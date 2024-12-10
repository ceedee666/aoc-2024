from pathlib import Path
from collections import deque
import typer

app = typer.Typer()

D = [1, -1, 1j, -1j]


def read_input_file(input_file_path: str) -> list:
    p = Path(input_file_path)

    with p.open() as f:
        lines = f.readlines()

    return [line.strip() for line in lines]


def parse(data: list[str]) -> dict[complex, int]:
    return {
        complex(i, j): int(c) for j, line in enumerate(data) for i, c in enumerate(line)
    }


def trail_score(p: complex, map: dict[complex, int], part_1: bool) -> int:
    if map[p] == 0:
        value = 0
        seen = set()
        seen.add(p)
        queue = deque()
        queue.append(p)
        while queue:
            c = queue.popleft()
            for d in D:
                next = c + d
                if next in map and map[next] == map[c] + 1 and next not in seen:
                    if map[c + d] == 9:
                        value += 1
                    else:
                        queue.append(next)

                    if part_1:
                        seen.add(next)
        return value
    else:
        return 0


def trail_scores(map: dict[complex, int], part_1: bool) -> list[int]:
    return [trail_score(k, map, part_1) for k in map]


def solve(data: list[str], part_1: bool = True) -> int:
    map = parse(data)
    scores = trail_scores(map, part_1)
    return sum(scores)


@app.command()
def part_1(input_file: str = "input.txt"):
    data = read_input_file(input_file)
    print(f"The score of all trailheads is {solve(data)}")


@app.command()
def part_2(input_file: str = "input.txt"):
    data = read_input_file(input_file)
    print(f"The score of all trailheads is {solve(data, False)}")


if __name__ == "__main__":
    app()
