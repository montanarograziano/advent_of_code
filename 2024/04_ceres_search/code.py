"""AoC 4, 2024."""

# Standard library imports
import pathlib
import sys

INPUT_FILE = "input.txt"


def parse_data(puzzle_input: str):
    """Parse input."""
    return puzzle_input.splitlines()


def part1(data):
    """Solve part 1."""
    res = 0
    ROWS, COLS = len(data), len(data[0])
    for r in range(ROWS):
        for c in range(COLS):
            if data[r][c] != "X":
                continue

            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if dr == dc == 0:
                        continue
                    if r + 3 * dr in range(ROWS) and c + 3 * dc in range(COLS):
                        if (
                            data[r + dr][c + dc] == "M"
                            and data[r + 2 * dr][c + 2 * dc] == "A"
                            and data[r + 3 * dr][c + 3 * dc] == "S"
                        ):
                            res += 1

    return res


def part2(data):
    """Solve part 2."""
    res = 0
    ROWS, COLS = len(data), len(data[0])
    for r in range(1, ROWS - 1):
        for c in range(1, COLS - 1):
            if data[r][c] != "A":
                continue

            corners = [
                data[r - 1][c - 1],
                data[r - 1][c + 1],
                data[r + 1][c + 1],
                data[r + 1][c - 1],
            ]
            if "".join(corners) in ["MMSS", "MSSM", "SSMM", "SMMS"]:
                res += 1

    return res


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
