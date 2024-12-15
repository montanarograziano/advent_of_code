"""AoC 15, 2024."""

# Standard library imports
import pathlib
import sys
from copy import deepcopy

INPUT_FILE = "input.txt"


def parse_data(puzzle_input: str):
    """Parse input."""
    return puzzle_input.split("\n\n")


def part1(data):
    """Solve part 1."""
    grid, moves = data
    grid = [list(line) for line in grid.splitlines()]
    moves = "".join(moves.splitlines())
    start = (-1, -1)
    rows, cols = len(grid), len(grid[0])
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == "@":
                start = (i, j)
                break
    r, c = start
    for move in moves:
        dr = {"^": -1, "v": 1}.get(move, 0)
        dc = {"<": -1, ">": 1}.get(move, 0)
        targets = [(r, c)]
        cr, cc = r, c
        go = True
        while True:
            cr += dr
            cc += dc
            char = grid[cr][cc]
            if char == "#":
                go = False
                break
            if char == "O":
                targets.append((cr, cc))
            if char == ".":
                break

        if not go:
            continue

        grid[r][c] = "."
        grid[r + dr][c + dc] = "@"
        for br, bc in targets[1:]:
            grid[br + dr][bc + dc] = "O"
        r, c = r + dr, c + dc

    print(*grid)
    return sum(
        100 * r + c for r in range(rows) for c in range(cols) if grid[r][c] == "O"
    )


def part2(data):
    """Solve part 2."""
    grid, moves = data
    expansion = {"#": "##", "O": "[]", ".": "..", "@": "@."}
    grid = [
        list("".join(expansion[char] for char in line)) for line in grid.splitlines()
    ]
    moves = "".join(moves.splitlines())
    start = (-1, -1)
    rows, cols = len(grid), len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == "@":
                start = (i, j)
                break

    r, c = start
    for move in moves:
        dr = {"^": -1, "v": 1}.get(move, 0)
        dc = {"<": -1, ">": 1}.get(move, 0)
        targets = [(r, c)]
        go = True
        for cr, cc in targets:
            nr = cr + dr
            nc = cc + dc
            if (nr, nc) in targets:
                continue
            char = grid[nr][nc]
            if char == "#":
                go = False
                break
            if char == "[":
                targets.append((nr, nc))
                targets.append((nr, nc + 1))
            if char == "]":
                targets.append((nr, nc))
                targets.append((nr, nc - 1))

        if not go:
            continue

        copy = deepcopy(grid)
        grid[r][c] = "."
        grid[r + dr][c + dc] = "@"
        for br, bc in targets[1:]:
            grid[br][bc] = "."
        for br, bc in targets[1:]:
            grid[br + dr][bc + dc] = copy[br][bc]
        r += dr
        c += dc

    return sum(
        100 * r + c for r in range(rows) for c in range(cols) if grid[r][c] == "["
    )


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
