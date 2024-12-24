"""AoC 24, 2024."""

# Standard library imports
import pathlib
import re
import sys
from collections import deque

INPUT_FILE = "input.txt"


def parse_data(puzzle_input: str):
    """Parse input."""
    first, second = puzzle_input.split("\n\n")
    inps = {x.split(": ")[0]: int(x.split(": ")[1]) for x in first.split("\n")}
    # x00 AND y00 -> z00 # Parse a string like this
    gates = re.findall(r"(\w{3}) (AND|XOR|OR) (\w{3}) -> (\w{3})", second)
    return inps, gates


def process(op, a, b):
    if op == "AND":
        return a & b
    if op == "OR":
        return a | b
    if op == "XOR":
        return a ^ b
    raise ValueError("Invalid operation")


def solve_p1(inps, gates):
    delay = deque(gates)
    while delay:
        a, op, b, out = delay.popleft()
        if a not in inps or b not in inps:
            delay.append((a, op, b, out))
            continue
            # raise ValueError("No input value for a or b")
        inps[out] = process(op, inps[a], inps[b])
    return inps


def part1(data):
    """Solve part 1."""
    inps, gates = data
    inps = solve_p1(inps, gates)
    result = []
    final_bits = []
    for k, v in inps.items():
        if k.startswith("z"):
            final_bits.append((int(k[1:]), v))
    final_bits.sort(reverse=True)
    for fb in final_bits:
        result.append(fb[1])
    return int("".join(str(x) for x in result), 2)


def part2(data):
    """Solve part 2."""
    inps, gates = data
    q = deque(gates)
    wrong = set()
    highest_z = "z00"
    for a, op, b, out in gates:
        if out[0] == "z" and int(out[1:]) > int(highest_z[1:]):
            highest_z = out
    for a, op, b, out in gates:
        if out.startswith("z") and op != "XOR" and out != highest_z:
            wrong.add(out)
        if (
            op == "XOR"
            and out[0] not in ["x", "y", "z"]
            and a[0] not in ["x", "y", "z"]
            and b[0] not in ["x", "y", "z"]
        ):
            wrong.add(out)
        if op == "AND" and "x00" not in [a, b]:
            for sub_a, sub_op, sub_b, sub_out in gates:
                if (out == sub_a or out == sub_b) and sub_op != "OR":
                    wrong.add(out)
        if op == "XOR":
            for sub_a, sub_op, sub_b, sub_res in gates:
                if (out == sub_a or out == sub_b) and sub_op == "OR":
                    wrong.add(out)

    while q:
        a, op, b, out = q.popleft()
        if a in inps and b in inps:
            inps[out] = process(op, inps[a], inps[b])
        else:
            q.append((a, op, b, out))

    return ",".join(sorted(wrong))


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
