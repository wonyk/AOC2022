#!/usr/bin/env python3

from collections import defaultdict

def part1(size_dict):
    P1_MAX_SIZE = 100000

    p1_result = 0

    for file_sizes in size_dict.values():
        if file_sizes <= P1_MAX_SIZE:
            p1_result += file_sizes

    return p1_result


def part2(size_dict):
    TOTAL_SIZE = 70000000
    REQUIRED_SIZE = 30000000

    p2_result = REQUIRED_SIZE

    unused_size = TOTAL_SIZE - size_dict[""]
    size_to_clear = REQUIRED_SIZE - unused_size

    if size_to_clear <= 0:
        return 0

    for sizes in size_dict.values():
        if sizes >= size_to_clear and sizes < p2_result:
            p2_result = sizes

    return p2_result


def main():
    inp = open("input", "r").read().splitlines()

    DIR_SIZE = defaultdict(int)
    DIR_LIST = []

    for line in inp:
        match line.split():
            case ["$", "cd", ".."]:
                DIR_LIST.pop()
            case ["$", "cd", dir]:
                if dir == "/":
                    DIR_LIST = [""]
                else:
                    path_after = f"{DIR_LIST[-1]}/{dir}"
                    DIR_LIST.append(path_after)
            case ["dir", _]:
                continue
            case ["$", "ls"]:
                continue
            case [file_size, _]:
                for dir in DIR_LIST:
                    DIR_SIZE[dir] += int(file_size)

    p1_result = part1(DIR_SIZE)
    print(f"Part 1: {p1_result}")

    p2_result = part2(DIR_SIZE)
    print(f"Part 2: {p2_result}")


if __name__ == "__main__":
    main()
