#!/usr/bin/env python3

from collections import deque
from copy import deepcopy

# Indexes
NUM_TO_MOVE_IDX = 1
FROM_IDX = 3
TO_IDX = 5


def part1(stacks, instructions):

    for instr in instructions:
        tokens = instr.split()
        num_move = int(tokens[NUM_TO_MOVE_IDX])
        origin = int(tokens[FROM_IDX]) - 1
        dest = int(tokens[TO_IDX]) - 1

        for _ in range(num_move):
            stacks[dest].append(stacks[origin].pop())

    p1_result = ""

    for deques in stacks:
        p1_result += deques.pop()

    return p1_result


def part2(stacks, instructions):

    for instr in instructions:
        tokens = instr.split()
        num_move = int(tokens[NUM_TO_MOVE_IDX])
        origin = int(tokens[FROM_IDX]) - 1
        dest = int(tokens[TO_IDX]) - 1
        intermediate = deque()

        for _ in range(num_move):
            intermediate.append(stacks[origin].pop())

        for _ in range(num_move):
            stacks[dest].append(intermediate.pop())

    p2_result = ""

    for deques in stacks:
        p2_result += deques.pop()

    return p2_result


def main():
    inp = open("input", "r").read().splitlines()
    num_stacks = (len(inp[0]) + 1) // 4

    stacks = [deque() for _ in range(num_stacks)]
    sep_idx = inp.index("")
    instructions = inp[sep_idx + 1 :]

    for i in range(sep_idx):
        start_idx = 0
        row = inp[i]

        while (next_bracket := row.find("[", start_idx)) != -1:
            stacks[next_bracket // 4].appendleft(row[next_bracket + 1])
            start_idx = next_bracket + 1

    p1_result = part1(deepcopy(stacks), instructions)
    print(f"Part 1: {p1_result}")

    p2_result = part2(deepcopy(stacks), instructions)
    print(f"Part 2: {p2_result}")


if __name__ == "__main__":
    main()
