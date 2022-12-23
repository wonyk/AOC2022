#!/usr/bin/env python3

from copy import deepcopy
import z3


def bottom_up(num_monkey: dict, op_monkey: dict):
    while op_monkey:
        temp = deepcopy(op_monkey)
        for pending in op_monkey:
            l, o, r = op_monkey[pending].split()
            if l in num_monkey and r in num_monkey:
                n1 = num_monkey[l]
                n2 = num_monkey[r]
                if o == "+":
                    result = n1 + n2
                elif o == "-":
                    result = n1 - n2
                elif o == "*":
                    result = n1 * n2
                else:
                    result = n1 / n2

                num_monkey[pending] = result
                del temp[pending]
        op_monkey = temp


def part1(num_monkey: dict, op_monkey: dict):
    bottom_up(num_monkey, op_monkey)
    return num_monkey["root"]


def part2(num_monkey: dict, op_monkey: dict):
    humn = z3.Real("humn")
    num_monkey["humn"] = humn

    root_l, _, root_r = op_monkey["root"].split()
    del op_monkey["root"]

    bottom_up(num_monkey, op_monkey)

    num1 = num_monkey[root_l]
    num2 = num_monkey[root_r]

    s = z3.Solver()
    s.add(num1 == num2)
    s.check()
    m = s.model()
    return m[humn]


def main():
    inp = open("input", "r").read().splitlines()

    number_monkey = {}
    operator_monkey = {}

    for line in inp:
        monkey, job = line.split(": ")
        if job.isnumeric():
            number_monkey[monkey] = int(job)
        else:
            operator_monkey[monkey] = job

    p1_result = part1(deepcopy(number_monkey), deepcopy(operator_monkey))
    print(f"Part 1: {round(p1_result)}")

    p2_result = part2(deepcopy(number_monkey), deepcopy(operator_monkey))
    print(f"Part 2: {p2_result}")


if __name__ == "__main__":
    main()
