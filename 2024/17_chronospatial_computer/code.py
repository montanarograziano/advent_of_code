"""AoC 17, 2024."""

# Standard library imports
import pathlib
import re
import sys

INPUT_FILE = "input.txt"


def parse_data(puzzle_input: str):
    """Parse input."""
    a, b, c, *program = list(map(int, re.findall(r"(\d+)", puzzle_input)))
    return a, b, c, program


def compute(regs, program):
    ptr = 0
    output = []
    while ptr < len(program):
        ins, op = program[ptr : ptr + 2]
        if 0 <= op <= 3:
            combo = op
        elif op == 4:
            combo = regs[0]
        elif op == 5:
            combo = regs[1]
        elif op == 6:
            combo = regs[2]

        match ins:
            case 0:
                regs[0] = regs[0] // 2**combo
            case 1:
                regs[1] = regs[1] ^ op
            case 2:
                regs[1] = combo % 8
            case 3:
                ptr = ptr + 2 if regs[0] == 0 else op - 2
            case 4:
                regs[1] = regs[1] ^ regs[2]
            case 5:
                output.append(combo % 8)
            case 6:
                regs[1] = regs[0] // 2**combo
            case 7:
                regs[2] = regs[0] // 2**combo
        ptr += 2
    return output


def part1(data):
    register_a = data[0]
    register_b = data[1]
    register_c = data[2]
    regs = [register_a, register_b, register_c]
    program = data[3]
    return ",".join(list(map(str, compute(regs, program))))


def recursive(regs, program, n=0, d=15):
    res = [1e20]
    if d == -1:
        return n
    for i in range(8):
        nn = n + i * 8**d
        regs = [nn, 0, 0]
        output = compute(regs, program)
        if len(output) != len(program):
            continue
        if output[d] == program[d]:
            res.append(recursive(regs, program, nn, d - 1))
    return min(res)


def part2(data) -> int:
    register_a = data[0]
    register_b = data[1]
    register_c = data[2]
    regs = [register_a, register_b, register_c]
    program = data[3]
    return recursive(regs, program)


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
