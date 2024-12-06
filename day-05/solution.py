from functools import partial, cmp_to_key
from typing import Callable
from pathlib import Path

from click import pass_obj
import typer

app = typer.Typer()


def read_input_file(input_file_path: str) -> list:
    p = Path(input_file_path)

    with p.open() as f:
        lines = f.readlines()

    return [line.strip() for line in lines]


def parse(data: list[str]) -> tuple[list[tuple[int, int]], list[list[int]]]:
    idx = data.index("")

    rule_data = data[:idx]
    rule_data = [r.split("|") for r in rule_data]
    rules = [(int(r[0]), int(r[1])) for r in rule_data]

    update_data = data[idx + 1 :]
    updates = [list(map(int, u.split(","))) for u in update_data]
    return rules, updates


def is_correctly_ordered(update: list[int], compare_fn: Callable) -> bool:
    return update == sorted(update, key=cmp_to_key(compare_fn))


def compare_with_rules(rules: list[tuple[int, int]], x: int, y: int):
    return -1 if (x, y) in rules else 1


def solve(data: list[str], part_2: bool = False) -> int:
    rules, updates = parse(data)
    compare = partial(compare_with_rules, rules)

    if part_2:
        incorrect = list(
            filter(lambda u: not (is_correctly_ordered(u, compare)), updates)
        )
        updates = [sorted(u, key=cmp_to_key(compare)) for u in incorrect]

    else:
        updates = list(
            filter(
                lambda u: is_correctly_ordered(u, compare),
                updates,
            )
        )
    return sum([c[len(c) // 2] for c in updates])


@app.command()
def part_1(input_file: str):
    data = read_input_file(input_file)
    print(f"The sum of the middle page number is {solve(data)}")


@app.command()
def part_2(input_file: str):
    data = read_input_file(input_file)
    print(
        f"The sum of the middle page number of the correct updates is {solve(data, True)}"
    )


if __name__ == "__main__":
    app()
