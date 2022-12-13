#!/usr/bin/env python3

from ast import literal_eval
from functools import cmp_to_key


def compare(l, r):
    match l,r:
        case int(), int():
            if l > r:
                return -1
            elif r > l:
                return 1
            return 0
        case int(), list():
            return compare([l], r)
        case list(), int():
            return compare(l, [r])
        case list(), list():
            for ele_left, ele_right in zip(l, r):
                results = compare(ele_left, ele_right)
                if results == 0:
                    continue
                return results
            if len(l) < len(r):
                return 1
            elif len(l) == len(r):
                return 0
            else:
                return -1

def part1(packets):
    p1_result = 0

    for i, p in enumerate(packets, start=1):
        if compare(*p) == 1:
            p1_result += i
        
    return p1_result
        


def part2(packets):

    p2_result = 0

    mixed_list = []
    for p in packets:
        mixed_list.append(p[0])
        mixed_list.append(p[1])
    
    mixed_list.append([[2]])
    mixed_list.append([[6]])

    # Sort using a custom sort function
    sorted_signals = sorted(mixed_list, key=cmp_to_key(compare))[::-1]
    idx_first = sorted_signals.index([[2]]) + 1
    idx_second = sorted_signals.index([[6]]) + 1

    return idx_first * idx_second


def main():
    inp = open("input", "r").read().strip().split("\n\n")

    packets = []
    for pairs in inp:
        l1, l2 = pairs.split("\n")
        packets.append([literal_eval(l1), literal_eval(l2)])

    p1_result = part1(packets)
    print(f"Part 1: {p1_result}")

    p2_result = part2(packets)
    print(f"Part 2: {p2_result}")


if __name__ == "__main__":
    main()
