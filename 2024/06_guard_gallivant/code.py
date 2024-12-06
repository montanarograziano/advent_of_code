"""AoC 6, 2024."""

# Standard library imports
import pathlib
import sys

INPUT_FILE = "input.txt"


def parse_data(puzzle_input: str):
    """Parse input."""
    grid = puzzle_input.splitlines()
    return [list(row) for row in grid]


def part1(data):
    """Solve part 1."""
    start = (-1, -1)

    ROWS, COLS = len(data), len(data[0])
    for i in range(ROWS):
        for j in range(COLS):
            if data[i][j] == "^":
                start = (i, j)
                break
    x, y = start
    visited = set()
    dx, dy = -1, 0

    while True:
        visited.add((x, y))
        nx, ny = x + dx, y + dy
        if nx not in range(ROWS) or ny not in range(COLS):
            break
        if data[nx][ny] != "#":
            x += dx
            y += dy
        else:
            dx, dy = dy, -dx

    return len(visited), visited


def loop(data, r, c):
    ROWS, COLS = len(data), len(data[0])
    visited = set()
    dr, dc = -1, 0
    while True:
        visited.add((r, c, dr, dc))
        nr, nc = r + dr, c + dc
        if nr not in range(ROWS) or nc not in range(COLS):
            break
        if data[nr][nc] != "#":
            r += dr
            c += dc
        else:
            dr, dc = dc, -dr
        if (r, c, dr, dc) in visited:
            return True


def part2(data):
    """Solve part 2."""
    ROWS, COLS = len(data), len(data[0])
    for i in range(ROWS):
        for j in range(COLS):
            if data[i][j] == "^":
                start = (i, j)
                break
    x, y = start
    result = 0
    empty = part1(data)[1]
    for i, j in empty:
        data[i][j] = "#"
        if loop(data, x, y):
            result += 1
        data[i][j] = "."

    return result


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    yield part1(parse_data(puzzle_input))[0]
    yield part2(parse_data(puzzle_input))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        path = sys.argv[1]
        print(f"\n{path}:")
        solutions = solve(puzzle_input=pathlib.Path(path).read_text().rstrip())
        print("\n".join(str(solution) for solution in solutions))
    else:
        solutions = solve(puzzle_input=pathlib.Path(INPUT_FILE).read_text().rstrip())
        print("\n".join(str(solution) for solution in solutions))
