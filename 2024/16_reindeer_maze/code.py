"""AoC 16, 2024."""

# Standard library imports
import heapq
import pathlib
import sys
from collections import defaultdict

from pyparsing import deque

INPUT_FILE = "input.txt"


def parse_data(puzzle_input: str):
    """Parse input."""
    return [list(line) for line in puzzle_input.splitlines()]


def part1(grid):
    """Solve part 1."""
    rows, cols = len(grid), len(grid[0])
    start, end = (-1, -1), (-1, -1)
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == "S":
                start = (row, col)
            if grid[row][col] == "E":
                end = (row, col)

    score = float("inf")
    pq = [(0, start[0], start[1], 0, 1)]
    seen = {(start[0], start[1], 0, 1)}
    while pq:
        cost, r, c, dr, dc = heapq.heappop(pq)
        seen.add((r, c, dr, dc))
        if (r, c) == end:
            score = min(score, cost)
        for new_cost, nr, nc, ndr, ndc in [
            (cost + 1, r + dr, c + dc, dr, dc),
            (cost + 1000, r, c, dc, -dr),
            (cost + 1000, r, c, -dc, dr),
        ]:
            if grid[nr][nc] == "#" or (nr, nc, ndr, ndc) in seen:
                continue
            heapq.heappush(pq, (new_cost, nr, nc, ndr, ndc))

    return score


def part2(grid):
    """Solve part 2."""
    rows, cols = len(grid), len(grid[0])
    start, end = (-1, -1), (-1, -1)
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == "S":
                start = (row, col)
            if grid[row][col] == "E":
                end = (row, col)

    pq = [(0, start[0], start[1], 0, 1)]
    lowest_cost = defaultdict(lambda: float("inf"))
    lowest_cost[(start[0], start[1], 0, 1)] = 0
    best_cost = float("inf")
    backtrack: dict[tuple, set] = {}
    end_states = set()
    while pq:
        cost, r, c, dr, dc = heapq.heappop(pq)
        if cost > lowest_cost[(r, c, dr, dc)]:
            continue
        if (r, c) == end:
            if cost > best_cost:
                break
            best_cost = cost
            end_states.add((r, c, dr, dc))

        for new_cost, nr, nc, ndr, ndc in [
            (cost + 1, r + dr, c + dc, dr, dc),
            (cost + 1000, r, c, dc, -dr),
            (cost + 1000, r, c, -dc, dr),
        ]:
            if grid[nr][nc] == "#":
                continue
            lowest = lowest_cost[(nr, nc, ndr, ndc)]
            if new_cost > lowest:
                continue
            if new_cost < lowest:
                backtrack[(nr, nc, ndr, ndc)] = set()
                lowest_cost[(nr, nc, ndr, ndc)] = new_cost
            backtrack[(nr, nc, ndr, ndc)].add((r, c, dr, dc))
            heapq.heappush(pq, (new_cost, nr, nc, ndr, ndc))

    states = deque(end_states)
    seen = set(end_states)
    while states:
        key = states.popleft()
        for last in backtrack.get(key, []):
            if last in seen:
                continue
            seen.add(last)
            states.append(last)

    return len({(r, c) for r, c, _, _ in seen})


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
