from pathlib import Path
import typer
import re
from operator import mul
from functools import reduce

app = typer.Typer()


def read_input_file(input_file_path: str) -> list[str]:
    p = Path(input_file_path)

    with p.open() as f:
        lines = f.readlines()

    return [line.strip() for line in lines]


def move(
    robot: tuple[tuple[int, int], tuple[int, int]],
    hight: int,
    width: int,
    seconds: int = 100,
) -> tuple[tuple[int, int], tuple[int, int]]:
    pos, speed = robot
    x, y = pos
    dx, dy = speed
    x += seconds * dx
    y += seconds * dy
    x %= hight
    y %= width
    return ((x, y), (dx, dy))


def count_robots_in_quadrants(
    robots: list[tuple[tuple[int, int], tuple[int, int]]], height: int, width: int
) -> tuple[int, int, int, int]:
    idx_h = height // 2
    idx_w = width // 2

    q1 = len([r for r in robots if r[0][0] < idx_w and r[0][1] < idx_h])
    q2 = len([r for r in robots if r[0][0] > idx_w and r[0][1] < idx_h])
    q3 = len([r for r in robots if r[0][0] < idx_w and r[0][1] > idx_h])
    q4 = len([r for r in robots if r[0][0] > idx_w and r[0][1] > idx_h])
    return q1, q2, q3, q4


def solve(
    data: list[str], hight: int = 103, width: int = 101, part: int = 1
) -> tuple[int, list[tuple[tuple[int, int], tuple[int, int]]]]:
    numbers = [re.findall(r"-?\d+", line) for line in data]
    robots = [((int(x), int(y)), (int(dx), int(dy))) for x, y, dx, dy in numbers]

    if part == 1:
        robots = [move(r, width, hight) for r in robots]
        robots_in_qs = count_robots_in_quadrants(robots, hight, width)
        return reduce(mul, robots_in_qs), robots
    else:
        seconds = 0
        while len(robots) > len({p for p, _ in robots}):
            robots = [move(r, width, hight, 1) for r in robots]
            seconds += 1
        return seconds, robots


def print_robots(robots):
    positions = {p for p, _ in robots}

    image = ""
    for j in range(101):
        line = ""
        for i in range(103):
            if (i, j) in positions:
                line += "*"
            else:
                line += " "
        line += "\n"
        image += line

    print(image)


@app.command()
def part_1(input_file: str = "input.txt"):
    data = read_input_file(input_file)
    factor, _ = solve(data)
    print(f"The safety factor is {factor}")


@app.command()
def part_2(input_file: str = "input.txt"):
    data = read_input_file(input_file)
    seconds, robots = solve(data, part=2)
    print(f"The tree appears after {seconds} seconds.")
    print_robots(robots)


if __name__ == "__main__":
    app()
