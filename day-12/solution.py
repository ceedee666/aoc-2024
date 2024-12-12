from pathlib import Path
import typer
from collections import deque

app = typer.Typer()

D = [1, -1, 1j, -1j]


def read_input_file(input_file_path: str) -> list[str]:
    p = Path(input_file_path)

    with p.open() as f:
        lines = f.readlines()

    return [line.strip() for line in lines]


def parse(data: list[str]) -> list[set[complex]]:
    plants = {i + j * 1j: c for j, line in enumerate(data) for i, c in enumerate(line)}
    visited = set()
    regions = []
    for pos in plants:
        if pos not in visited:
            visited |= {pos}
            region = {pos}
            queue = deque([pos])
            while queue:
                c = queue.popleft()
                for d in D:
                    next = c + d
                    if next in plants and plants[next] == plants[c]:
                        if next not in visited:
                            visited |= {next}
                            region |= {next}
                            queue.append(next)
            regions.append(region)

    return regions


def neighbors(pos: complex, region: set[complex]) -> int:
    return sum(pos + d in region for d in D)


def primeter(region: set[complex], part: int = 1) -> int:
    if part == 1:
        return sum(4 - neighbors(pos, region) for pos in region)
    else:
        r_parts, i_parts = [n.real for n in region], [n.imag for n in region]
        min_i, max_i, min_j, max_j = (
            int(min(r_parts)),
            int(max(r_parts)),
            int(min(i_parts)),
            int(max(i_parts)),
        )

        sides = 0

        # Tracing rows
        prev_in, prev_out = set(), set()
        for j in range(min_j, max_j + 2):
            current_in, current_out = set(), set()
            for i in range(min_i - 1, max_i + 2):
                current = i + 1j * j
                next = current + 1

                # entering area
                if current not in region and next in region:
                    current_in |= {next}
                    if next - 1j not in prev_in:
                        sides += 1

                # exiting area
                if current in region and next not in region:
                    current_out |= {current}
                    if current - 1j not in prev_out:
                        sides += 1

            prev_in, prev_out = current_in, current_out

        # Tracing cols
        prev_in, prev_out = set(), set()
        for i in range(min_i, max_i + 2):
            current_in, current_out = set(), set()
            for j in range(min_j - 1, max_j + 2):
                current = i + 1j * j
                next = current + 1j

                # entering area
                if current not in region and next in region:
                    current_in |= {next}
                    if next - 1 not in prev_in:
                        sides += 1

                # exiting area
                if current in region and next not in region:
                    current_out |= {current}
                    if current - 1 not in prev_out:
                        sides += 1

            prev_in, prev_out = current_in, current_out

        return sides


def solve(data: list[str], part: int = 1) -> int:
    regions = parse(data)
    return sum(len(r) * primeter(r, part) for r in regions)


@app.command()
def part_1(input_file: str = "input.txt"):
    data = read_input_file(input_file)
    print(f"The price of the fences is {solve(data)}")


@app.command()
def part_2(input_file: str = "input.txt"):
    data = read_input_file(input_file)
    print(f"The price of the fences with discount is {solve(data, 2)}")


if __name__ == "__main__":
    app()
