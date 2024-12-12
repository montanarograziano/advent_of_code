"""AoC 12, 2024."""

# Standard library imports
import pathlib
import sys
from collections import defaultdict

INPUT_FILE = "input.txt"


def parse_data(puzzle_input: str):
    """Parse input."""
    return puzzle_input.splitlines()


def part1(grid):
    """Solve part 1."""
    visit = set()
    res = 0
    adj = defaultdict(int)
    groups = defaultdict(set)
    rows, cols = len(grid), len(grid[0])

    def dfs(r, c, group):
        if r not in range(rows) or c not in range(cols) or (r, c) in visit:
            return

        visit.add((r, c))
        groups[group].add((r, c))
        for dr, dc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
            if (
                dr not in range(rows)
                or dc not in range(cols)
                or grid[dr][dc] != grid[r][c]
            ):
                continue
            adj[r, c] += 1
            if (dr, dc) not in visit:
                dfs(dr, dc, group)

    idx = 0
    for r in range(rows):
        for c in range(cols):
            if (r, c) not in visit:
                g = (grid[r][c], idx)
                dfs(r, c, g)
                idx += 1

    for group in groups:
        area = len(groups[group])
        perimeter = 4 * area - sum(adj[coord] for coord in groups[group])
        # print(group, area, perimeter, area * perimeter)
        res += area * perimeter

    return res


def part2(data):
    """Solve part 2."""


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
