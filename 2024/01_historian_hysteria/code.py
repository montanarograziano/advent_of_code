"""AoC 1, 2024."""

# Standard library imports
import pathlib
import sys

INPUT_FILE = "input.txt"


def parse_data(puzzle_input: str):
    """Parse input."""
    return [list(map(int, x.split())) for x in puzzle_input.splitlines()]


def part1(data):
    left, right = [list(x) for x in zip(*data)]
    return sum(abs(x - y) for x, y in zip(sorted(left), sorted(right)))


def part2(data):
    left, right = [list(x) for x in zip(*data)]
    return sum(x * right.count(x) for x in left)


def solve(puzzle_input):
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
