#!/usr/bin/env python3

import re

# import z3

Y = 2000000
LIMIT = 4000000
# Y = 10
# LIMIT = 20


def part1(data, beacons, no_beacons, man_dists):

    for sx, sy, bx, by in data:
        if by == Y:
            beacons.add((bx, by))

        man_distance = abs(by - sy) + abs(bx - sx)
        man_dists.append(man_distance)

        min_dist = abs(Y - sy)

        for direction in (-1, 1):
            for i in range(man_distance - min_dist + 1):
                no_beacons.add((sx + (i * direction), Y))

    p1_result = len(no_beacons) - len(beacons)

    return p1_result


def part2(data, man_dists):

    for dist, (sx, sy, _, _) in zip(man_dists, data):
        for p in range(dist + 1):
            borders = [
                (sx - dist - 1 + p, sy - p),
                (sx + dist + 1 - p, sy - p),
                (sx - dist - 1 + p, sy + p),
                (sx + dist + 1 - p, sy + p),
            ]

            for bx, by in borders:
                if not 0 <= bx <= LIMIT or not 0 <= by <= LIMIT:
                    continue
                if not all(
                    abs(bx - ax) + abs(by - ay) > man_dists[i]
                    for i, (ax, ay, _, _) in enumerate(data)
                ):
                    continue
                else:
                    return bx * 4000000 + by

    return None


# Obtained from Reddit answers to test and learn Z3
# def z3abs(x):
#     return z3.If(x >= 0, x, -x)


# def part2(data, man_dists):
#     s = z3.Solver()
#     x = z3.Int("x")
#     y = z3.Int("y")
#     s.add(x >= 0)
#     s.add(x <= 4000000)
#     s.add(y >= 0)
#     s.add(y <= 4000000)
#     for dist, (sx, sy, _, _) in zip(man_dists, data):
#         s.add(z3abs(x - sx) + z3abs(y - sy) > dist)

#     s.check()
#     model = s.model()
#     return model[x].as_long() * 4000000 + model[y].as_long()


def main():
    inp = open("input", "r").read().splitlines()
    # inp = open("test", "r").read().splitlines()

    data = []
    man_dists = []

    beacons = set()
    no_beacons = set()

    for line in inp:
        numbers = re.findall("-?\d+", line)
        data.append(list(map(int, numbers)))

    p1_result = part1(data, beacons, no_beacons, man_dists)
    print(f"Part 1: {p1_result}")

    p2_result = part2(data, man_dists)
    print(f"Part 2: {p2_result}")


if __name__ == "__main__":
    main()
