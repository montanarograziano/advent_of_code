"""AoC 10, 2024."""

# Standard library imports
import pathlib
import sys
from collections import deque

INPUT_FILE = "input.txt"


def parse_data(puzzle_input: str):
    """Parse input."""
    return [list(map(int, line)) for line in puzzle_input.splitlines()]


def part1(data):
    """Solve part 1."""
    res = 0
    rows, cols = len(data), len(data[0])
    trails = [(r, c) for r in range(rows) for c in range(cols) if data[r][c] == 0]

    def dfs(r, c, visit):
        nonlocal res
        if r < 0 or r >= rows or c < 0 or c >= cols or (r, c) in visit:
            return
        visit.add((r, c))
        if data[r][c] == 9:
            res += 1
            return

        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if (
                nr in range(rows)
                and nc in range(cols)
                and (nr, nc) not in visit
                and data[nr][nc] == data[r][c] + 1
            ):
                dfs(nr, nc, visit)

    for r, c in trails:
        dfs(r, c, set())

    return res


def part2(data):
    """Solve part 2."""
    rows, cols = len(data), len(data[0])
    trails = [(r, c) for r in range(rows) for c in range(cols) if data[r][c] == 0]

    def bfs(grid, r, c):
        seen = {(r, c): 1}
        q = deque([(r, c)])
        res = 0
        while len(q) > 0:
            cr, cc = q.popleft()
            if grid[cr][cc] == 9:
                res += seen[(cr, cc)]
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nr, nc = cr + dr, cc + dc
                if (
                    nr in range(rows)
                    and nc in range(cols)
                    and grid[nr][nc] == grid[cr][cc] + 1
                ):
                    if (nr, nc) in seen:
                        seen[(nr, nc)] += seen[(cr, cc)]
                        continue
                    seen[(nr, nc)] = seen[(cr, cc)]
                    q.append((nr, nc))
        return res

    return sum(bfs(data, r, c) for r, c in trails)


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
