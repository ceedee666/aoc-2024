from pathlib import Path
import typer


app = typer.Typer()


def read_input_file(input_file_path: str) -> list:
    p = Path(input_file_path)

    with p.open() as f:
        lines = f.readlines()

    return [line.strip() for line in lines]


def parse(data: list[str]) -> list[list[int]]:
    return list(map(lambda x: list(map(int, x.split(" "))), data))


def calculate_differences(report: list[int]) -> list[int]:
    diffs = [x - y for x, y in zip(report, report[1:])]
    return diffs


def check_report(report: list[int]) -> bool:
    diffs = calculate_differences(report)
    return all([1 <= x <= 3 for x in diffs]) or all([-3 <= x <= -1 for x in diffs])


def check_reports(
    reports: list[list[int]], allow_one_error: bool = False
) -> list[bool]:
    if allow_one_error:
        report_variants = all_report_variants(reports)
        checked_report_variants = [check_reports(r) for r in report_variants]
        safe_reports = [any(v) for v in checked_report_variants]
    else:
        safe_reports = [check_report(r) for r in reports]
    return safe_reports


def report_variants(report: list[int]) -> list[list[int]]:
    return [report[0:i] + report[i + 1 :] for i in range(len(report))]


def all_report_variants(reports: list[list[int]]) -> list[list[list[int]]]:
    return [report_variants(r) for r in reports]


def solve_part_1(data: list[str]) -> int:
    reports = parse(data)
    checked = check_reports(reports)
    return checked.count(True)


def solve_part_2(data: list[str]) -> int:
    reports = parse(data)
    checked = check_reports(reports, True)
    return checked.count(True)


@app.command()
def part_1(input_file: str):
    data = read_input_file(input_file)
    print(f"The number of safe reports is: {solve_part_1(data)}")


@app.command()
def part_2(input_file: str):
    data = read_input_file(input_file)
    print(f"The number of safe reports is: {solve_part_2(data)}")


if __name__ == "__main__":
    app()
