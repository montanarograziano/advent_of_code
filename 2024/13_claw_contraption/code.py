"""AoC 13, 2024."""

# Standard library imports
import pathlib
import re
import sys

INPUT_FILE = "input.txt"


def parse_data(puzzle_input: str):
    """Parse input."""
    return puzzle_input.split("\n\n")


def part1(data):
    """Solve part 1."""
    res = 0
    for block in data:
        ax, ay, bx, by, px, py = map(int, re.findall(r"\d+", block))
        score = float("inf")
        for i in range(101):
            for j in range(101):
                if ax * i + bx * j == px and ay * i + by * j == py:
                    score = min(score, 3 * i + j)
        if score != float("inf"):
            res += score

    return res


def part2(data):
    """Solve part 2."""
    res = 0
    for block in data:
        ax, ay, bx, by, px, py = map(int, re.findall(r"\d+", block))
        px += 10000000000000
        py += 10000000000000
        ca = (px * by - py * bx) / (ax * by - ay * bx)
        cb = (px - ax * ca) / bx
        if ca % 1 == cb % 1 == 0:
            res += 3 * int(ca) + int(cb)

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
