#!/usr/bin/env python3

MIN_CHARS_PACKET = 4
MIN_CHARS_MESSAGE = 14


def has_duplicate(substr, min_length):
    return len(set(substr)) < min_length


def check_str(inp, min_length):
    for i in range(len(inp)):
        substr = inp[i : i + min_length]
        if not has_duplicate(substr, min_length):
            return i + min_length

    return None


def part1(inp):
    return check_str(inp, MIN_CHARS_PACKET)


def part2(inp):
    return check_str(inp, MIN_CHARS_MESSAGE)


def main():
    inp = open("input", "r").read().splitlines()
    challenge_str = inp[0]

    p1_result = part1(challenge_str)
    print(f"Part 1: {p1_result}")

    p2_result = part2(challenge_str)
    print(f"Part 2: {p2_result}")


if __name__ == "__main__":
    main()
