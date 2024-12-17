import re
from collections import defaultdict
from pathlib import Path

import typer

app = typer.Typer()


def read_input_file(input_file_path: str) -> list[str]:
    p = Path(input_file_path)

    with p.open() as f:
        lines = f.readlines()

    return [line.strip() for line in lines]


def parse(data: list[str]) -> tuple[dict[str, int], list[tuple[int, int]], str]:
    values = [int(x) for x in re.findall(r"\d+", " ".join(data[:3]))]
    registers = {"A": values[0], "B": values[1], "C": values[2]}

    instr_values = data[-1].split(" ")[1].split(",")
    instr_values = [int(x) for x in instr_values]

    instructions = list(zip(instr_values[0::2], instr_values[1::2]))

    return registers, instructions, data[-1]


def combo_value(combo_operand: int, registers: dict[str, int]) -> int:
    match combo_operand:
        case 0 | 1 | 2 | 3:
            return combo_operand
        case 4:
            return registers["A"]
        case 5:
            return registers["B"]
        case 6:
            return registers["C"]
        case _:
            return -1


def execute_program(
    registers: dict[str, int], instructions: list[tuple[int, int]], ip: int = 0
) -> tuple[dict[str, int], list[int]]:
    out = []
    while ip < len(instructions):
        opcode, operand = instructions[ip]
        match opcode:
            case 0:
                registers["A"] = registers["A"] // 2 ** combo_value(operand, registers)
                ip += 1
            case 1:
                registers["B"] = registers["B"] ^ operand
                ip += 1
            case 2:
                registers["B"] = combo_value(operand, registers) % 8
                ip += 1
            case 3:
                if registers["A"] != 0:
                    ip = int(operand / 2)
                else:
                    ip += 1
            case 4:
                registers["B"] = registers["B"] ^ registers["C"]
                ip += 1
            case 5:
                out.append(combo_value(operand, registers) % 8)
                ip += 1
            case 6:
                registers["B"] = registers["A"] // 2 ** combo_value(operand, registers)
                ip += 1
            case 7:
                registers["C"] = registers["A"] // 2 ** combo_value(operand, registers)
                ip += 1

    return registers, out


def solve(data: list[str], part: int = 1) -> str:
    registers, instructions, original_program = parse(data)
    if part == 1:
        registers, out = execute_program(registers, instructions)
        return ",".join(str(x) for x in out)
    else:
        possible_reg_a_values = set(range(8))
        target = [i for inst in instructions for i in inst]
        for i in range(2, len(target) + 1):
            target_output = target[-i:]

            next_reg_a = set()

            for value_a in possible_reg_a_values:
                for value_b in range(8):
                    registers = defaultdict(int)
                    initial_value_reg_a = (value_a << 3) + value_b
                    registers["A"] = initial_value_reg_a
                    _, out = execute_program(registers, instructions)

                    if out == target_output:
                        next_reg_a.add(initial_value_reg_a)
            possible_reg_a_values = next_reg_a
        return str(min(possible_reg_a_values))


@app.command()
def part_1(input_file: str = "input.txt"):
    data = read_input_file(input_file)
    print(f"The output of the program is {solve(data)}")


@app.command()
def part_2(input_file: str = "input.txt"):
    data = read_input_file(input_file)
    print(f"The lowest value for register A is {solve(data,2)}")


if __name__ == "__main__":
    app()
