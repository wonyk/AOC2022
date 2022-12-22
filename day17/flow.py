#!/usr/bin/env python3

ROCKS = [
    [(2, 0), (3, 0), (4, 0), (5, 0)],
    [(3, 0), (2, 1), (3, 1), (4, 1), (3, 2)],
    [(2, 0), (3, 0), (4, 0), (4, 1), (4, 2)],
    [(2, 0), (2, 1), (2, 2), (2, 3)],
    [(2, 0), (2, 1), (3, 0), (3, 1)],
]

LEFT, RIGHT = "<", ">"
JET_MOVE = {LEFT: -1, RIGHT: 1}
TOWER_WIDTH = 7


def checkwall(rock, dx):
    for x, _ in rock:
        if not (0 <= x + dx < TOWER_WIDTH):
            return False
    return True


def checkrocks(rock, space, dx, dy):
    for x, y in rock:
        if (x + dx, y + dy) in space:
            return False
    return True


def move_x(rock, dx):
    return [(x + dx, y) for x, y in rock]


def move_y(rock, dy):
    return [(x, y + dy) for x, y in rock]


def get_snapshot(space, top):
    return frozenset([(x, top - y) for x, y in space if top - y <= 60])


def simulate(inp, num_rounds):
    space = {(x, 0) for x in range(TOWER_WIDTH)}
    top = 0
    jet_idx = 0
    round = 0
    repeat = 0
    num_rocks = len(ROCKS)
    num_jet = len(inp)
    SEEN = {}

    while round < num_rounds:
        rock_template = ROCKS[round % num_rocks]
        rock = [(x, y + top + 4) for (x, y) in rock_template]

        while True:
            move = JET_MOVE[inp[jet_idx]]
            jet_idx = (jet_idx + 1) % num_jet

            if checkwall(rock, move) and checkrocks(rock, space, move, dy=0):
                rock = move_x(rock, move)

            if not checkrocks(rock, space, dx=0, dy=-1):
                break

            rock = move_y(rock, -1)

        space.update(rock)
        top = max(top, max(y for _, y in rock))

        # Save a snapshot to check against in the order of:
        # 1. Jet blast direction index
        # 2. Rock involved
        # 3. How it looks like for the top 60 height
        r_key = (jet_idx, round % num_rocks, get_snapshot(space, top))

        if r_key in SEEN and round > 2022:
            round_in_cycle, height = SEEN[r_key]
            num_round_passed = round - round_in_cycle
            extra_height = top - height

            repeat_num = (num_rounds - round) // num_round_passed
            repeat += repeat_num * extra_height
            round += repeat_num * num_round_passed

        else:
            SEEN[r_key] = (round, top)

        round += 1

    return top + repeat


def part1(inp):
    num_rounds = 2022
    return simulate(inp, num_rounds)


def part2(inp):
    num_rounds = 1000000000000
    return simulate(inp, num_rounds)


def main():
    inp = open("input", "r").read().splitlines()[0]

    p1_result = part1(inp)
    print(f"Part 1: {p1_result}")

    p2_result = part2(inp)
    print(f"Part 2: {p2_result}")


if __name__ == "__main__":
    main()
