"""AoC 3, 2024."""

# Standard library imports
import pathlib
import re
import sys

INPUT_FILE = "input.txt"


def parse_data(puzzle_input: str):
    """Parse input."""
    return puzzle_input


def part1(data):
    """Solve part 1."""
    groups = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", data)
    return sum(int(x) * int(y) for x, y in groups)


def part2(data):
    """Solve part 2."""
    groups = re.findall(r"(do\(\)|don't\(\))|mul\((\d{1,3}),(\d{1,3})\)", data)
    result = 0
    skip = False
    for act, x, y in groups:
        if act == "don't()":
            skip = True
        elif act == "do()":
            skip = False
        else:
            if not skip:
                result += int(x) * int(y)

    return result


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
