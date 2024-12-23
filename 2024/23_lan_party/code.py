"""AoC 23, 2024."""

# Standard library imports
import pathlib
import sys
from collections import defaultdict

INPUT_FILE = "input.txt"


def parse_data(puzzle_input: str):
    """Parse input."""
    return [line.split("-") for line in puzzle_input.splitlines()]


def find_triples(lans):
    # Find all sets of three interconnected nodes
    # starting from lans which a dict that contains as key a node and as value a list of neighbours
    triples = set()
    for node in lans:
        for neighbour in lans[node]:
            for neighbour2 in lans[neighbour]:
                if node != neighbour2 and neighbour2 in lans[node]:
                    triples.add(tuple(sorted([node, neighbour, neighbour2])))
    return triples

def search(node, lans, req):
    for neighbor in lans[node]:
        if neighbor in req:
            continue
        if all(neighbor in lans[query] for query in req):
            continue
        




def part1(data):
    """Solve part 1."""
    lans = defaultdict(set)
    for left, right in data:
        lans[right].add(left)
        lans[left].add(right)

    triples: set[list[str]] = find_triples(lans)
    print(len([s for s in triples if any(cn.startswith("t") for cn in s)]))


def part2(data):
    """Solve part 2."""
    lans = defaultdict(set)
    for left, right in data:
        lans[right].add(left)
        lans[left].add(right)

    triples: set[list[str]] = find_triples(lans)
    print(len([s for s in triples if all(cn.startswith("t") for cn in s)]))


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
