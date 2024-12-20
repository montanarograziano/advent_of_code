"""AoC 20, 2024."""

# Standard library imports
import pathlib
import sys

INPUT_FILE = "input.txt"


def parse_data(puzzle_input: str):
    """Parse input."""
    return [list(line) for line in puzzle_input.splitlines()]


def part1(grid):
    """Solve part 1."""
    rows, cols = len(grid), len(grid[0])
    dists = [[-1] * cols for _ in range(rows)]
    r, c = -1, -1
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == "S":
                r, c = row, col
                break

    dists[r][c] = 0
    while grid[r][c] != "E":
        for nr, nc in [(r + 1, c), (r, c + 1), (r - 1, c), (r, c - 1)]:
            if (
                nr in range(rows)
                and nc in range(cols)
                and dists[nr][nc] == -1
                and grid[nr][nc] != "#"
            ):
                dists[nr][nc] = dists[r][c] + 1
                r, c = nr, nc

    result = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "#":
                continue
            for nr, nc in [
                (r + 2, c),
                (r + 1, c + 1),
                (r, c + 2),
                (r - 1, c + 1),
            ]:
                if nr < 0 or nc < 0 or nr >= rows or nc >= rows:
                    continue
                if grid[nr][nc] == "#":
                    continue
                if abs(dists[r][c] - dists[nr][nc]) >= 102:
                    result += 1

    return result


def part2(grid):
    """Solve part 2."""
    rows, cols = len(grid), len(grid[0])
    dists = [[-1] * cols for _ in range(rows)]
    r, c = -1, -1
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == "S":
                r, c = row, col
                break

    dists[r][c] = 0
    while grid[r][c] != "E":
        for nr, nc in [(r + 1, c), (r, c + 1), (r - 1, c), (r, c - 1)]:
            if (
                nr in range(rows)
                and nc in range(cols)
                and dists[nr][nc] == -1
                and grid[nr][nc] != "#"
            ):
                dists[nr][nc] = dists[r][c] + 1
                r, c = nr, nc

    result = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "#":
                continue
            for radius in range(2, 21):
                for dr in range(radius + 1):
                    dc = radius - dr
                    for nr, nc in {
                        (r + dr, c + dc),
                        (r + dr, c - dc),
                        (r - dr, c + dc),
                        (r - dr, c - dc),
                    }:
                        if nr < 0 or nc < 0 or nr >= rows or nc >= rows:
                            continue
                        if grid[nr][nc] == "#":
                            continue
                        if dists[r][c] - dists[nr][nc] >= 100 + radius:
                            result += 1

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
