"""AoC 18, 2024."""

# Standard library imports
import pathlib
import sys
from collections import deque
from copy import deepcopy

INPUT_FILE = "input.txt"


def parse_data(puzzle_input: str):
    """Parse input."""
    return [
        (int(line.split(",")[1]), int(line.split(",")[0]))
        for line in puzzle_input.splitlines()
    ]


def bfs(grid):
    rows, cols = len(grid), len(grid[0])
    q = deque([(0, 0, 0)])
    visit = set()
    visit.add((0, 0))
    while q:
        r, c, steps = q.popleft()
        grid[r][c] = "O"
        if r == rows - 1 and c == cols - 1:
            return steps
        for dr, dc in [(r + 1, c), (r, c + 1), (r, c - 1), (r - 1, c)]:
            if (
                dr not in range(rows)
                or dc not in range(cols)
                or (dr, dc) in visit
                or grid[dr][dc] == "#"
            ):
                continue
            visit.add((dr, dc))
            q.append((dr, dc, steps + 1))
    return -1


def part1(data):
    """Solve part 1."""
    rows, cols = (71, 71)
    subset = 1024
    grid = [["."] * cols for _ in range(rows)]
    for x, y in data[:subset]:
        grid[x][y] = "#"

    return bfs(deepcopy(grid))


def part2(data):
    """Solve part 2."""
    rows, cols = (71, 71)
    grid = [["."] * cols for _ in range(rows)]
    for x, y in data:
        grid[x][y] = "#"
        if bfs(deepcopy(grid)) == -1:
            # print(*grid, sep="\n")
            return y, x


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
