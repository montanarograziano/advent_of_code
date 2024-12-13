"""AoC 8, 2024."""

# Standard library imports
import pathlib
import sys
from collections import defaultdict

INPUT_FILE = "input.txt"


def parse_data(puzzle_input: str):
    """Parse input."""
    return [line.strip() for line in puzzle_input.splitlines()]


def part1(data):
    """Solve part 1."""
    rows, cols = len(data), len(data[0])
    antennas = defaultdict(list)
    for r, row in enumerate(data):
        for c, cell in enumerate(row):
            if cell != ".":
                antennas[cell].append((r, c))

    antinodes = set()
    for array in antennas.values():
        for i in range(len(array)):
            for j in range(i + 1, len(array)):
                r1, c1 = array[i]
                r2, c2 = array[j]
                antinodes.add((2 * r1 - r2, 2 * c1 - c2))
                antinodes.add((2 * r2 - r1, 2 * c2 - c1))

    return len([0 for r, c in antinodes if 0 <= r < rows and 0 <= c < cols])


def part2(data):
    """Solve part 2."""
    rows, cols = len(data), len(data[0])
    antennas = defaultdict(list)
    for r, row in enumerate(data):
        for c, cell in enumerate(row):
            if cell != ".":
                antennas[cell].append((r, c))

    antinodes = set()
    for array in antennas.values():
        for i in range(len(array)):
            for j in range(len(array)):
                if i == j:
                    continue
                r1, c1 = array[i]
                r2, c2 = array[j]
                dr, dc = r2 - r1, c2 - c1
                r = r1
                c = c1
                while 0 <= r < rows and 0 <= c < cols:
                    antinodes.add((r, c))
                    r += dr
                    c += dc

    return len(antinodes)


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
