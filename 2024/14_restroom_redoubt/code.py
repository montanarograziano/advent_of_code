"""AoC 14, 2024."""

# Standard library imports
import pathlib
import re
import sys

import matplotlib.pyplot as plt
import numpy as np

INPUT_FILE = "input.txt"


def parse_data(puzzle_input: str):
    """Parse input."""
    return puzzle_input.splitlines()


def part1(data):
    """Solve part 1."""
    rows, cols = 103, 101
    grid = [[0 for _ in range(cols)] for _ in range(rows)]
    for line in data:
        p, v = re.findall(r"(-?\d+),(-?\d+)", line)
        px, py = list(map(int, p))
        vx, vy = list(map(int, v))
        for _ in range(100):
            px = (px + vx) % cols
            py = (py + vy) % rows

        grid[py][px] += 1

    q1, q2, q3, q4 = 0, 0, 0, 0
    for i in range(rows):
        for j in range(cols):
            mx, my = cols // 2, rows // 2
            if i < my and j < mx:
                q1 += grid[i][j]
            elif i < my and j > mx:
                q3 += grid[i][j]
            elif i > my and j < mx:
                q2 += grid[i][j]
            elif i > my and j > mx:
                q4 += grid[i][j]

    return q1 * q2 * q3 * q4


def part2(data):
    """Solve part 2."""
    rows, cols = 103, 101
    grid = [[0 for _ in range(cols)] for _ in range(rows)]
    robots = []
    for line in data:
        p, v = re.findall(r"(-?\d+),(-?\d+)", line)
        px, py = list(map(int, p))
        vx, vy = list(map(int, v))
        robots.append([px, py, vx, vy])
        grid[py][px] += 1

    seconds = 0

    def is_tree(grid):
        return all(x < 2 for line in grid for x in line)

    for i in range(10000):  # seems to work, just to prevent infinite loop
        for i, (px, py, vx, vy) in enumerate(robots):
            nx = (px + vx) % cols
            ny = (py + vy) % rows
            robots[i] = [nx, ny, vx, vy]

            grid[py][px] -= 1
            grid[ny][nx] += 1

        seconds += 1
        if is_tree(grid):
            plt.imshow(np.array(grid), cmap="viridis", interpolation="nearest")
            plt.show()
            return seconds


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
