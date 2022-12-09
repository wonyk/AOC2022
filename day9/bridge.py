#!/usr/bin/env python3


def check_and_move(x_head, y_head, x_tail, y_tail) -> tuple:
    # nearby
    if abs(x_head - x_tail) <= 1 and abs(y_head - y_tail) <= 1:
        new_tail = (x_tail, y_tail)
    else:
        # same row
        if y_head == y_tail:
            new_x = (x_head + x_tail) // 2
            new_tail = (new_x, y_tail)
        # same col
        elif x_head == x_tail:
            new_y = (y_head + y_tail) // 2
            new_tail = (x_tail, new_y)
        else:
            new_x = x_tail + 1 if x_head > x_tail else x_tail - 1
            new_y = y_tail + 1 if y_head > y_tail else y_tail - 1
            new_tail = (new_x, new_y)

    return new_tail


def get_new_pos(x_head, y_head, x_tail, y_tail, direction, is_head=True):
    if not is_head:
        new_head = (x_head, y_head)
    elif direction == "R":
        new_head = (x_head + 1, y_head)
    elif direction == "L":
        new_head = (x_head - 1, y_head)
    elif direction == "U":
        new_head = (x_head, y_head + 1)
    else:
        new_head = (x_head, y_head - 1)

    new_tail = check_and_move(*new_head, x_tail, y_tail)

    did_change = False if new_tail == (x_tail, y_tail) else True

    return new_head, new_tail, did_change


def part1(inp):
    VISITED = set()

    head_pos = (0, 0)
    tail_pos = (0, 0)

    VISITED.add(tail_pos)

    for instruction in inp:
        direction, num_steps = instruction.split()
        for _ in range(int(num_steps)):
            head_pos, tail_pos, _ = get_new_pos(*head_pos, *tail_pos, direction)
            VISITED.add(tail_pos)

    return len(VISITED)


def part2(inp):

    VISITED = set()
    NUM_LINKS = 10

    POS = [(0, 0) for _ in range(NUM_LINKS)]

    VISITED.add(POS[-1])

    for instruction in inp:
        direction, num_steps = instruction.split()
        for _ in range(int(num_steps)):
            is_head = True
            for i in range(NUM_LINKS - 1):
                pos_front = POS[i]
                pos_back = POS[i + 1]
                POS[i], POS[i + 1], did_change = get_new_pos(
                    *pos_front, *pos_back, direction, is_head
                )

                if not did_change:
                    break

                is_head = False

            VISITED.add(POS[-1])

    return len(VISITED)


def main():
    inp = open("input", "r").read().splitlines()

    p1_result = part1(inp)
    print(f"Part 1: {p1_result}")

    p2_result = part2(inp)
    print(f"Part 2: {p2_result}")


if __name__ == "__main__":
    main()
