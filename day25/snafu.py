#!/usr/bin/env python3

BASE_SNAFU = {"2": 2, "1": 1, "0": 0, "-": -1, "=": -2}
SNAFU = "=-012"


def calc_total(inp):
    total = 0

    for line in inp:
        sum = 0
        for c in line:
            sum *= 5
            sum += BASE_SNAFU[c]
        total += sum

    return total


def dec2snafu(num):
    if num == 0:
        return ""
    num += 2
    return dec2snafu(num // 5) + SNAFU[num % 5]


def main():
    inp = open("input", "r").read().splitlines()

    total = calc_total(inp)

    p1_result = dec2snafu(total)
    print(f"Final ans: {p1_result}")


if __name__ == "__main__":
    main()
