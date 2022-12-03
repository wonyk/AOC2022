#!/usr/bin/env python3


def calculate_priority(chara):
    lower_a = ord("a")
    upper_a = ord("A")

    if chara.isupper():
        return ord(chara) - upper_a + 27
    else:
        return ord(chara) - lower_a + 1


def part1(inp):
    p1_result = 0

    for rucksack in inp:
        length = len(rucksack)
        first_comp = rucksack[: length // 2]
        second_comp = rucksack[length // 2 :]

        assert len(first_comp) == len(second_comp)

        first_items = set(first_comp)
        second_items = set(second_comp)
        common_item = iter(first_items.intersection(second_items))
        p1_result += calculate_priority(next(common_item))

    return p1_result


def part2(inp):
    assert len(inp) % 3 == 0

    p2_result = 0
    for i in range(0, len(inp), 3):
        items1 = set(inp[i])
        items2 = set(inp[i + 1])
        items3 = set(inp[i + 2])

        common_item = iter(items1.intersection(items2, items3))
        p2_result += calculate_priority(next(common_item))

    return p2_result


def main():
    inp = open("input", "r").read().splitlines()

    p1_result = part1(inp)
    print(f"Part 1: {p1_result}")

    p2_result = part2(inp)
    print(f"Part 2: {p2_result}")


if __name__ == "__main__":
    main()
