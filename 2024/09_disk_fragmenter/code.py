"""AoC 9, 2024."""

# Standard library imports
import pathlib
import sys

INPUT_FILE = "input.txt"


def parse_data(puzzle_input: str):
    """Parse input."""
    return puzzle_input.strip()


def process_data(data):
    disk = []
    fid = 0
    for i, char in enumerate(data):
        x = int(char)
        if i % 2 == 0:
            disk += [fid] * x
            fid += 1
        else:
            disk += [-1] * x

    return disk


def part1(data):
    """Solve part 1."""
    disk = process_data(data)

    blanks = [i for i, x in enumerate(disk) if x == -1]
    for i in blanks:
        if disk[-1] == -1:
            disk.pop()
        if i >= len(disk):
            break
        disk[i] = disk.pop()

    return sum(i * n for i, n in enumerate(disk))


def part2(data):
    """Solve part 2."""
    files = {}
    blanks = []

    fid = 0
    pos = 0

    for i, char in enumerate(data):
        x = int(char)
        if i % 2 == 0:
            if x == 0:
                raise ValueError("unexpected x=0 for file")
            files[fid] = (pos, x)
            fid += 1
        else:
            if x != 0:
                blanks.append((pos, x))
        pos += x

    while fid > 0:
        fid -= 1
        pos, size = files[fid]
        for i, (start, length) in enumerate(blanks):
            if start >= pos:
                blanks = blanks[:i]
                break
            if size <= length:
                files[fid] = (start, size)
                if size == length:
                    blanks.pop(i)
                else:
                    blanks[i] = (start + size, length - size)
                break

    total = 0

    for fid, (pos, size) in files.items():
        for x in range(pos, pos + size):
            total += fid * x

    return total


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
