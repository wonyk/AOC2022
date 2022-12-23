#!/usr/bin/env python3


def mix(inp: list, rounds=1):
    size = len(inp)
    indices = [i for i in range(size)]

    for _ in range(rounds):
        for i, num in enumerate(inp):
            idx = indices.index(i)
            indices.pop(idx)
            new_idx = (idx + num) % (size - 1)
            indices.insert(new_idx, i)

    zero_idx = indices.index(inp.index(0))
    result = sum([inp[indices[(zero_idx + n) % size]] for n in (1000, 2000, 3000)])
    return result


def main():
    input = open("input", "r").read().splitlines()

    inp = list(map(int, input))

    p1_result = mix(inp)
    print(f"Part 1: {p1_result}")

    KEY = 811589153
    inp = [i * KEY for i in inp]

    p2_result = mix(inp, rounds=10)
    print(f"Part 2: {p2_result}")


if __name__ == "__main__":
    main()
