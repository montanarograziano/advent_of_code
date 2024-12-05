"""AoC 5, 2024."""

# Standard library imports
import pathlib
import sys
from collections import defaultdict, deque

INPUT_FILE = "input.txt"


def parse_data(puzzle_input: str):
    """Parse input."""
    return puzzle_input


def split_parts(data: str) -> tuple:
    first, second = data.split("\n\n")
    first = first.splitlines()
    second = second.splitlines()
    return first, second


def part1(data: str):
    """Solve part 1."""
    first, second = split_parts(data)
    order = defaultdict(set)
    for line in first:
        l, r = line.split("|")
        order[r].add(l)
    result = 0
    wrong_id = set()
    for i, line in enumerate(second):
        nums = line.split(",")
        nums_set = set(nums)
        wrong = False
        cur = set()
        for n in nums:
            pre = order[n].intersection(nums_set)
            # print("cur", cur, "pre", pre, pre.issubset(cur))
            # all nums in pre should have been already in cur
            if not pre.issubset(cur):
                wrong = True
                wrong_id.add(i)
            cur.add(n)

        # sum the middle number in the sequence
        if not wrong:
            result += int(nums[len(nums) // 2])

    return result, wrong_id


def part2(data):
    """Solve part 2."""
    _, wrong_idx = part1(data)
    first, second = split_parts(data)
    order = defaultdict(set)
    for line in first:
        l, r = line.split("|")
        order[r].add(l)

    result = 0
    for i in list(wrong_idx):
        nums = deque(second[i].split(","))
        nums_set = set(nums)
        cur = []
        while nums:
            pre = order[nums[0]].intersection(nums_set)
            if pre.issubset(cur):
                cur.append(nums.popleft())
            else:
                nums.rotate(-1)

        result += int(cur[len(cur) // 2])

    return result


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse_data(puzzle_input)
    yield part1(data)[0]
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
