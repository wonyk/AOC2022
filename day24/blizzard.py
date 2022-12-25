#!/usr/bin/env python3

from functools import cache

HEIGHT = None
WIDTH = None
blitz = []


@cache
def get_blitz(time):
    forbidden = set()
    for x, y, (dx, dy) in blitz:
        forbidden.add(((x + dx * time) % WIDTH, (y + dy * time) % HEIGHT))
    return forbidden


def shift(pos, forbidden):
    t = []
    x, y = pos

    for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1), (0, 0)]:
        nx = x + dx
        ny = y + dy
        if (nx, ny) not in forbidden:
            t.append((nx, ny))
    return t


def filter_valid(pos, start, goal):
    x, y = pos
    if (x % WIDTH == x and y % HEIGHT == y) or (x, y) in [start, goal]:
        return True
    return False


def bfs(start, goal, start_time):
    seen = set()
    todo = [(start, start_time)]

    while todo:
        pos, time = todo.pop(0)
        time += 1

        # Use the same trick to reduce the size of time
        blitz_state = get_blitz(time % (WIDTH * HEIGHT))
        next_move = shift(pos, blitz_state)
        next_move = [p for p in next_move if filter_valid(p, start, goal)]

        for move in next_move:
            if (move, time) in seen:
                continue
            elif move == goal:
                return time
            else:
                seen.add((move, time))
                todo.append((move, time))


def part2(inp):

    p2_result = 0

    return p2_result


def main():
    global WIDTH, HEIGHT, blitz

    inp = open("input", "r").read().splitlines()

    HEIGHT = len(inp) - 2
    WIDTH = len(inp[0]) - 2

    HOME = (0, -1)
    GOAL = (WIDTH - 1, HEIGHT)
    DIR = {"<": (-1, 0), ">": (1, 0), "v": (0, 1), "^": (0, -1)}

    for y, row in enumerate(inp):
        for x, col in enumerate(row):
            if col in ">v^<":
                blitz.append((x - 1, y - 1, DIR[col]))

    p1_result = bfs(HOME, GOAL, 0)
    print(f"Part 1: {p1_result}")

    total_2trip = bfs(GOAL, HOME, p1_result)
    p2_result = bfs(HOME, GOAL, total_2trip)
    print(f"Part 2: {p2_result}")


if __name__ == "__main__":
    main()
