"""AoC 19, 2024."""

# Standard library imports
import pathlib
import sys

INPUT_FILE = "input.txt"


def parse_data(puzzle_input: str):
    """Parse input."""
    available, onsen = puzzle_input.split("\n\n")
    return available, onsen


def dfs(line: str, idx, patterns, cache):
    # Try each element in pattern if it matches in line, the remove the token and try the rest of the string
    # until it's consumed
    if idx == len(line):
        return True

    if (line, idx) in cache:
        return cache[(line, idx)]

    cache[(line, idx)] = False
    for pattern in patterns:
        if line.startswith(pattern, idx):
            if dfs(line, idx + len(pattern), patterns, cache):
                cache[(line, idx)] = True
                return True

    return cache[(line, idx)]


def dfs2(line: str, idx, patterns, cache, combinations):
    if idx == len(line):
        return 1

    if (line, idx) in cache:
        return cache[(line, idx)]

    cache[(line, idx)] = 0
    for pattern in patterns:
        if line.startswith(pattern, idx):
            cache[(line, idx)] += dfs2(
                line, idx + len(pattern), patterns, cache, combinations
            )

    combinations[line] = cache[(line, idx)]
    return cache[(line, idx)]


def part1(data: tuple[str, str]):
    """Solve part 1."""
    available = data[0].strip().split(", ")
    onsen = data[1].splitlines()
    patterns = set(available)
    result = 0
    cache = {}
    for line in onsen:
        if dfs(line, 0, patterns, cache):
            result += 1

    return result


def part2(data):
    """Solve part 2."""
    available = data[0].strip().split(", ")
    onsen = data[1].splitlines()
    patterns = set(available)
    result = 0
    cache = {}
    combinations = {}
    for line in onsen:
        dfs2(line, 0, patterns, cache, combinations)
        result += combinations.get(line, 0)

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
