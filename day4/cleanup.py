#!/usr/bin/env python3

LOWER_BOUND_IDX = 0
UPPER_BOUND_IDX = 1


def check_contained(less_work, more_work):
    return (
        more_work[UPPER_BOUND_IDX] >= less_work[UPPER_BOUND_IDX]
        and more_work[LOWER_BOUND_IDX] <= less_work[LOWER_BOUND_IDX]
    )


def check_overlap(lower_end, higher_end):
    return higher_end[LOWER_BOUND_IDX] <= lower_end[UPPER_BOUND_IDX]


def split_and_int(ranges):
    return [int(x) for x in ranges.split("-")]


def part1(inp):
    p1_result = 0

    for pairs in inp:
        formatted = [split_and_int(pair) for pair in pairs.split(",")]
        elf1, elf2 = formatted[0], formatted[1]

        num_assigned_e1 = elf1[UPPER_BOUND_IDX] - elf1[LOWER_BOUND_IDX] + 1
        num_assigned_e2 = elf2[UPPER_BOUND_IDX] - elf2[LOWER_BOUND_IDX] + 1

        if num_assigned_e2 > num_assigned_e1:
            is_contained = check_contained(elf1, elf2)
        else:
            is_contained = check_contained(elf2, elf1)

        if is_contained:
            p1_result += 1

    return p1_result


def part2(inp):

    p2_result = 0

    for pairs in inp:
        formatted = [split_and_int(pair) for pair in pairs.split(",")]
        elf1, elf2 = formatted[0], formatted[1]

        if elf1[UPPER_BOUND_IDX] < elf2[UPPER_BOUND_IDX]:
            overlap = check_overlap(elf1, elf2)
        else:
            overlap = check_overlap(elf2, elf1)

        if overlap:
            p2_result += 1

    return p2_result


def main():
    inp = open("input", "r").read().splitlines()

    p1_result = part1(inp)
    print(f"Part 1: {p1_result}")

    p2_result = part2(inp)
    print(f"Part 2: {p2_result}")


if __name__ == "__main__":
    main()
