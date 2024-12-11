"""AoC 11, 2024."""

# Standard library imports
import pathlib
import sys
from functools import cache

INPUT_FILE = "input.txt"


def parse_data(puzzle_input: str):
    """Parse input."""
    return [int(x) for x in puzzle_input.split()]


def solve_stones(data, n):
    for i in range(n):
        output = []
        for stone in data:
            if stone == 0:
                output.append(1)
                continue
            string = str(stone)
            length = len(string)
            if length % 2 == 0:
                output.append(int(string[: length // 2]))
                output.append(int(string[length // 2 :]))
            else:
                output.append(stone * 2024)
        data = output
    return len(data)


def part1(data):
    """Solve part 1."""
    return solve_stones(data, 25)


@cache
def count(stone, steps):
    if steps == 0:
        return 1
    if stone == 0:
        return count(1, steps - 1)
    string = str(stone)
    length = len(string)
    if length % 2 == 0:
        return count(int(string[: length // 2]), steps - 1) + count(
            int(string[length // 2 :]), steps - 1
        )
    return count(stone * 2024, steps - 1)


def part2(data):
    """Solve part 2."""
    return sum(count(stone, 75) for stone in data)


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
