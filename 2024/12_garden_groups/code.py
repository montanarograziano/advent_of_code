"""AoC 12, 2024."""

# Standard library imports
import pathlib
import sys
from collections import deque

INPUT_FILE = "input.txt"


def bfs(r, c, region: set, seen: set, grid):
    rows, cols = len(grid), len(grid[0])
    q = deque([(r, c)])
    while q:
        r, c = q.popleft()
        if (r, c) in seen:
            continue
        seen.add((r, c))
        region.add((r, c))
        for dr, dc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
            if (
                dr not in range(rows)
                or dc not in range(cols)
                or grid[dr][dc] != grid[r][c]
            ):
                continue
            q.append((dr, dc))

    return region


def parse_data(puzzle_input: str):
    """Parse input."""
    return puzzle_input.splitlines()


def part1(grid):
    """Solve part 1."""
    rows, cols = len(grid), len(grid[0])
    seen = set()
    regions = []

    for r in range(rows):
        for c in range(cols):
            if (r, c) in seen:
                continue
            regions.append(bfs(r, c, set(), seen, grid))

    def perimeter(region):
        res = 0
        for r, c in region:
            res += 4
            for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                if (nr, nc) in region:
                    res -= 1
        return res

    return sum(len(region) * perimeter(region) for region in regions)


def part2(grid):
    """Solve part 2."""
    rows, cols = len(grid), len(grid[0])
    seen = set()
    regions = []
    mapping = dict()
    for row in range(rows):
        for col in range(cols):
            mapping[(row, col)] = grid[row][col]

    for r in range(rows):
        for c in range(cols):
            if (r, c) in seen:
                continue
            regions.append(bfs(r, c, set(), seen, grid))

    def sides(region):
        sides = 0
        for row, col in region:
            for i, j, adj_1, adj_2 in [
                (1, 1, (0, 1), (1, 0)),
                (1, -1, (0, -1), (1, 0)),
                (-1, 1, (0, 1), (-1, 0)),
                (-1, -1, (0, -1), (-1, 0)),
            ]:
                diag = ((row + i), (col + j))
                adj_1 = (row + adj_1[0], col + adj_1[1])
                adj_2 = (row + adj_2[0], col + adj_2[1])

                is_diag_out = diag not in mapping or diag not in region
                is_adj_1_out = adj_1 not in mapping or adj_1 not in region
                is_adj_2_out = adj_2 not in mapping or adj_2 not in region

                sides += bool(
                    (is_diag_out and is_adj_1_out and is_adj_2_out)
                    or (is_diag_out and not is_adj_1_out and not is_adj_2_out)
                    or (not is_diag_out and is_adj_1_out and is_adj_2_out)
                )
        return sides

    return sum(len(region) * sides(region) for region in regions)


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
