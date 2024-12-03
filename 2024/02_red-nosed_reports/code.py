"""AoC 2, 2024."""

# Standard library imports
import pathlib
import sys

INPUT_FILE = "input.txt"


def safe(row):
    diffs = [y - x for x, y in zip(row, row[1:])]
    return all(1 <= diff <= 3 for diff in diffs) or all(
        -3 <= diff <= -1 for diff in diffs
    )


def parse_data(puzzle_input: str):
    """Parse input."""
    return [list(map(int, row.split())) for row in puzzle_input.splitlines()]


def part1(data: list[list[int]]):
    """Solve part 1."""

    return sum(1 if safe(row) else 0 for row in data)


def part2(data):
    """Solve part 2."""

    return sum(
        1 if any(safe(row[:i] + row[i + 1 :]) for i in range(len(row))) else 0
        for row in data
    )


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse_data(puzzle_input)
    yield part1(data)
    yield part2(data)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        path = sys.argv[1]
        print(f"\n{path}:")
        solutions = solve(puzzle_input=pathlib.Path(path).read_text().rstrip())
        print("\n".join(str(solution) for solution in solutions))
    else:
        solutions = solve(puzzle_input=pathlib.Path(INPUT_FILE).read_text().rstrip())
        print("\n".join(str(solution) for solution in solutions))
