#!/usr/bin/env python3


def get_neighbours(coords):
    neighbour = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
    x, y, z = coords
    for dx, dy, dz in neighbour:
        yield (x + dx, y + dy, z + dz)


def part1(inp):
    sides = 0
    CUBES = set()

    for line in inp:
        coords = tuple(map(int, line.split(",")))
        neighbours = get_neighbours(coords)
        sides += 6

        num_neighbour = 0
        for n in neighbours:
            if n in CUBES:
                num_neighbour += 1

        sides -= num_neighbour * 2
        CUBES.add(coords)

    return CUBES, sides


def part2(CUBES):

    min_x, max_x = min(x for x, y, z in CUBES) - 1, max(x for x, y, z in CUBES) + 1
    min_y, max_y = min(y for x, y, z in CUBES) - 1, max(y for x, y, z in CUBES) + 1
    min_z, max_z = min(z for x, y, z in CUBES) - 1, max(z for x, y, z in CUBES) + 1

    queue = [(min_x, min_y, min_z)]
    seen = set()
    area = 0

    while queue:
        x, y, z = queue.pop()
        seen.add((x, y, z))

        for n in get_neighbours((x, y, z)):
            a, b, c = n
            if min_x <= a <= max_x and min_y <= b <= max_y and min_z <= c <= max_z:
                if n in seen:
                    continue
                if n in CUBES:
                    area += 1
                else:
                    seen.add(n)
                    queue.append(n)
    return area


def main():
    inp = open("input", "r").read().splitlines()
    # inp = open("test", "r").read().splitlines()

    CUBES, p1_result = part1(inp)
    print(f"Part 1: {p1_result}")

    p2_result = part2(CUBES)
    print(f"Part 2: {p2_result}")


if __name__ == "__main__":
    main()
