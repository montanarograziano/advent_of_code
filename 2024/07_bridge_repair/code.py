"""AoC 7, 2024."""

# Standard library imports
import pathlib
import sys

INPUT_FILE = "input.txt"


def parse_data(puzzle_input: str):
    """Parse input."""
    return puzzle_input.splitlines()


def part1(data):
    """Solve part 1."""
    res = 0
    for line in data:
        tot = int(line.split(": ")[0])
        parts = list(map(int, line.split(": ")[1].split(" ")))

        def backtrack(i, cur):
            nonlocal res
            if cur > tot:
                return
            if i == len(parts):
                if cur == tot:
                    res += tot
                    return True
                return

            if backtrack(i + 1, cur + parts[i]) or backtrack(i + 1, cur * parts[i]):
                return True

        backtrack(0, 0)

    return res


def part2(data):
    """Solve part 2."""
    res = 0
    for line in data:
        tot = int(line.split(": ")[0])
        parts = list(map(int, line.split(": ")[1].split(" ")))

        def backtrack(i, cur):
            nonlocal res
            if cur > tot:
                return
            if i == len(parts):
                if cur == tot:
                    res += tot
                    return True
                return
            if (
                backtrack(i + 1, cur + parts[i])
                or backtrack(i + 1, cur * parts[i])
                or backtrack(i + 1, int(str(cur) + str(parts[i])))
            ):
                return True

        backtrack(0, 0)

    return res


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
