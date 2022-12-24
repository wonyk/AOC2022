#!/usr/bin/env python3

from itertools import cycle
from collections import defaultdict
from copy import deepcopy

FOV = [
    [(-1, -1), (0, -1), (1, -1)],
    [(-1, 1), (0, 1), (1, 1)],
    [(-1, -1), (-1, 0), (-1, 1)],
    [(1, -1), (1, 0), (1, 1)],
]


def has_neighbour(elf, pos):
    neigh = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    x, y = elf
    check = [(x + a, y + b) in pos for (a, b) in neigh]
    return any(check)


def make_move(pos: set, direction):
    proposal = defaultdict(list)
    curr_dir = next(direction)
    for elf in pos:
        if not has_neighbour(elf, pos):
            continue

        x, y = elf
        for i in range(4):
            orientation = FOV[(i + curr_dir) % 4]
            for dx, dy in orientation:
                if (x + dx, y + dy) in pos:
                    break
            else:
                # Middle one is always the direction to go to (N/S/W/E)
                dx, dy = orientation[1]
                proposal[x + dx, y + dy].append(elf)
                break

    # Check if duplicate proposals
    for k, v in proposal.items():
        if len(v) > 1:
            continue
        pos.remove(v[0])
        pos.add(k)

    return len(proposal) != 0


def part1(position):
    direction = cycle(range(4))
    pos = deepcopy(position)

    for _ in range(10):
        make_move(pos, direction)

    xs = [e[0] for e in pos]
    ys = [e[1] for e in pos]
    minx = min(xs)
    miny = min(ys)
    maxx = max(xs) + 1
    maxy = max(ys) + 1

    total = (maxx - minx) * (maxy - miny)

    return total - len(pos)


def part2(position):

    p2_result = 1

    direction = cycle(range(4))
    pos = deepcopy(position)

    while make_move(pos, direction):
        p2_result += 1

    return p2_result


def main():
    inp = open("input", "r").read().splitlines()

    pos = set()

    for i, row in enumerate(inp):
        for j, col in enumerate(row):
            if col == "#":
                pos.add((j, i))

    p1_result = part1(pos)
    print(f"Part 1: {p1_result}")

    p2_result = part2(pos)
    print(f"Part 2: {p2_result}")


if __name__ == "__main__":
    main()
