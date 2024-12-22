"""AoC 22, 2024."""

# Standard library imports
import pathlib
import sys

INPUT_FILE = "input.txt"
PRUNE = 16777216
TO_GENERATE = 2000
maps = {}


def magic_num(n):
    for _ in range(TO_GENERATE):
        first = ((n * 64) ^ n) % PRUNE
        second = ((first // 32) ^ first) % PRUNE
        third = ((second * 2048) ^ second) % PRUNE
        n = third
    return n


def parse_data(puzzle_input: str):
    """Parse input."""
    return [int(line) for line in puzzle_input.splitlines()]


def part1(data):
    """Solve part 1."""
    result = 0
    for line in data:
        result += magic_num(line)
    return result


def best_score(n):
    nums = []
    diffs = []
    nums.append(n % 10)
    seen = set()
    for i in range(TO_GENERATE - 1):
        first = ((n * 64) ^ n) % PRUNE
        second = ((first // 32) ^ first) % PRUNE
        third = ((second * 2048) ^ second) % PRUNE
        n = third
        diffs.append((n % 10) - nums[-1])
        nums.append(n % 10)
    for i in range(4, len(nums)):
        a, b, c, d = diffs[i - 4], diffs[i - 3], diffs[i - 2], diffs[i - 1]
        if (a, b, c, d) not in seen:
            seen.add((a, b, c, d))
            maps[(a, b, c, d)] = maps.get((a, b, c, d), 0) + nums[i]


def part2(data):
    """Solve part 2."""
    for line in data:
        best_score(line)
    # pick the key of the maximum value from maps
    result = max(maps.values())
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
