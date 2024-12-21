from enum import Enum
from functools import cache
from itertools import permutations
from pathlib import Path

import typer

app = typer.Typer()

numpad = ["789", "456", "123", " 0A"]
NUMPAD = {
    key: (x, y)
    for y, line in enumerate(numpad)
    for x, key in enumerate(line)
    if key != " "
}

dirpad = [" ^A", "<v>"]
DIRPAD = {
    key: (x, y)
    for y, line in enumerate(dirpad)
    for x, key in enumerate(line)
    if key != " "
}

PADTYPE = Enum("padtype", ["numpad", "dirpad"])

DIRS = {"^": (0, -1), ">": (1, 0), "v": (0, 1), "<": (-1, 0)}


def read_input_file(input_file_path: str) -> list[str]:
    p = Path(input_file_path)

    with p.open() as f:
        lines = f.readlines()

    return [line.strip() for line in lines]


@cache
def keypresses(
    sequence: str, depth=2, dirkey: PADTYPE = PADTYPE.numpad, current_pos=None
) -> int:
    if not sequence:
        return 0

    match dirkey:
        case PADTYPE.numpad:
            keypad = NUMPAD
        case _:
            keypad = DIRPAD

    if not current_pos:
        current_pos = keypad["A"]

    step_x, step_y = current_pos
    target_x, target_y = keypad[sequence[0]]
    dx, dy = target_x - step_x, target_y - step_y

    buttons = ">" * dx + "<" * -dx + "v" * dy + "^" * -dy

    if depth:
        perm_lengths = []
        for perm in set(permutations(buttons)):
            step_x, step_y = current_pos
            path = []
            for button in perm:
                dx, dy = DIRS[button]
                step_x += dx
                step_y += dy
                path += [(step_x, step_y)]
            if all(p in keypad.values() for p in path):
                perm_lengths.append(
                    keypresses("".join(perm) + "A", depth - 1, PADTYPE.dirpad)
                )
        min_len = min(perm_lengths)
    else:
        min_len = len(buttons) + 1
    return min_len + keypresses(sequence[1:], depth, dirkey, (target_x, target_y))


def solve(codes: list[str], part: int = 1) -> int:
    if part == 1:
        return sum(keypresses(code, 2) * int(code[:-1]) for code in codes)
    else:
        return sum(keypresses(code, 25) * int(code[:-1]) for code in codes)


@app.command()
def part_1(input_file: str = "input.txt"):
    data = read_input_file(input_file)
    print(f"The sum of the complexities is {solve(data)}")


@app.command()
def part_2(input_file: str = "input.txt"):
    data = read_input_file(input_file)
    print(f"The sum of the complexities is {solve(data, 2)}")


if __name__ == "__main__":
    app()
