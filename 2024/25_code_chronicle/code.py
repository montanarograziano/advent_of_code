"""AoC 25, 2024."""

# Standard library imports
import pathlib
import sys

INPUT_FILE = "input.txt"


def parse_data(puzzle_input: str):
    """Parse input."""
    blocks = puzzle_input.split("\n\n")
    keys, locks = [], []
    for block in blocks:
        if block[0] == "#":
            locks.append(block.splitlines())
        else:
            keys.append(block.splitlines())

    return keys, locks


def part1(data):
    """Solve part 1."""
    keys, locks = data
    result = 0
    for lock in locks:
        for key in keys:
            h = len(lock)
            cols = len(lock[0])
            h_lock = [x.count("#") - 1 for x in zip(*lock)]
            h_key = [x.count("#") - 1 for x in zip(*key[::-1])]
            result += (
                1 if all(h_lock[i] + h_key[i] <= h - 2 for i in range(cols)) else 0
            )
    return result


def part2(data):
    """Solve part 2."""


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse_data(puzzle_input)
    yield part1(data)
    # yield part2(data)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        path = sys.argv[1]
        print(f"\n{path}:")
        solutions = solve(puzzle_input=pathlib.Path(path).read_text().rstrip())
        print("\n".join(str(solution) for solution in solutions))
    else:
        solutions = solve(puzzle_input=pathlib.Path(INPUT_FILE).read_text().rstrip())
        print("\n".join(str(solution) for solution in solutions))
