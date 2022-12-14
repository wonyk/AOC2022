#!/usr/bin/env python3


def add_sand(occupied, depth, part2=False):
    x, y = 500, 0

    if part2 and (x, y) in occupied:
        return False

    while True:
        y += 1

        if y == depth:
            if part2:
                occupied.add((x, y - 1))
                return True
            return False
        # fallthrough
        if (x, y) not in occupied:
            continue
        if (x - 1, y) not in occupied:
            x -= 1
            continue
        if (x + 1, y) not in occupied:
            x += 1
            continue

        occupied.add((x, y - 1))
        return True


def main():
    inp = open("input", "r").read().splitlines()

    occupied = set()
    depth = 0

    for line in inp:
        paths = [list(map(int, p.split(","))) for p in line.split(" -> ")]

        sx, sy = paths[0]
        for nx, ny in paths[1:]:
            if nx == sx:
                for i in range(min(sy, ny), max(sy, ny) + 1):
                    occupied.add((sx, i))
                depth = max(depth, max(sy, ny))
            else:
                for i in range(min(sx, nx), max(sx, nx) + 1):
                    occupied.add((i, sy))
                depth = max(depth, sy)
            sx, sy = nx, ny

    depth += 2

    p1_result = 0

    while add_sand(occupied, depth):
        p1_result += 1

    print(f"Part 1: {p1_result}")

    p2_result = p1_result

    while add_sand(occupied, depth, part2=True):
        p2_result += 1

    print(f"Part 2: {p2_result}")


if __name__ == "__main__":
    main()
