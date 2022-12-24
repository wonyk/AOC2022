#!/usr/bin/env python3

import re

X_MOVE = [1, 0, -1, 0]
Y_MOVE = [0, 1, 0, -1]
WIDTH = None
HEIGHT = None
RIGHT, DOWN, LEFT, UP = range(4)


def wrapped_leftpos(grid, y):
    for x in range(WIDTH):
        if (x, y) in grid:
            return x


def wrapped_rightpos(grid, y):
    for x in range(WIDTH - 1, -1, -1):
        if (x, y) in grid:
            return x


def wrapped_toppos(grid, x):
    for y in range(HEIGHT):
        if (x, y) in grid:
            return y


def wrapped_botpos(grid, x):
    for y in range(HEIGHT - 1, -1, -1):
        if (x, y) in grid:
            return y


def part1(grid, instr, start_x, start_y):
    dir = 0

    for i in instr:
        if i == "L":
            dir = (dir - 1) % 4
        elif i == "R":
            dir = (dir + 1) % 4
        else:
            dx = X_MOVE[dir]
            dy = Y_MOVE[dir]

            for _ in range(int(i)):
                newx = start_x + dx
                newy = start_y + dy

                if (newx, newy) not in grid:
                    if dir == RIGHT:
                        newx = wrapped_leftpos(grid, newy)
                    elif dir == LEFT:
                        newx = wrapped_rightpos(grid, newy)
                    elif dir == DOWN:
                        newy = wrapped_toppos(grid, newx)
                    else:
                        newy = wrapped_botpos(grid, newx)

                if grid[newx, newy] == "#":
                    break

                start_x = newx
                start_y = newy

    start_x += 1
    start_y += 1

    p1_result = 1000 * start_y + 4 * start_x + dir
    return p1_result


def get_face(x, y):
    if y < 50:
        if 50 <= x < 100:
            return 2, x - 50, y
        else:
            return 3, x - 100, y
    elif y < 100:
        return 1, x - 50, y - 50
    elif y < 150:
        if x < 50:
            return 5, x, y - 100
        else:
            return 4, x - 50, y - 100
    else:
        return 6, x, y - 150


def cubify_move(x, y, d):
    face, local_x, local_y = get_face(x, y)
    pos = None

    # Starting face
    if face == 2:
        if d == UP:
            newf = 6
            pos = 0, local_x + 150, RIGHT
        elif d == LEFT:
            newf = 5
            pos = 0, 149 - local_y, RIGHT
    elif face == 3:
        if d == UP:
            newf = 6
            pos = local_x, 199, UP
        elif d == DOWN:
            newf = 1
            pos = 99, local_x + 50, LEFT
        elif d == RIGHT:
            newf = 4
            pos = 99, 149 - local_y, LEFT
    elif face == 1:
        if d == LEFT:
            newf = 5
            pos = local_y, 100, DOWN
        elif d == RIGHT:
            newf = 3
            pos = 100 + local_y, 49, UP
    elif face == 5:
        if d == UP:
            newf = 1
            pos = 50, local_x + 50, RIGHT
        elif d == LEFT:
            newf = 2
            pos = 50, 49 - local_y, RIGHT
    elif face == 4:
        if d == RIGHT:
            newf = 3
            pos = 149, 49 - local_y, LEFT
        elif d == DOWN:
            newf = 6
            pos = 49, 150 + local_x, LEFT
    else:
        if d == LEFT:
            newf = 2
            pos = 50 + local_y, 0, DOWN
        elif d == RIGHT:
            newf = 4
            pos = 50 + local_y, 149, UP
        elif d == DOWN:
            newf = 3
            pos = local_x + 100, 0, DOWN

    return pos


def part2(grid, instr, start_x, start_y):

    dir = 0

    for i in instr:
        if i == "L":
            dir = (dir - 1) % 4
        elif i == "R":
            dir = (dir + 1) % 4
        else:

            for _ in range(int(i)):
                dx = X_MOVE[dir]
                dy = Y_MOVE[dir]

                newx = start_x + dx
                newy = start_y + dy
                newd = dir

                if (newx, newy) not in grid:
                    newx, newy, newd = cubify_move(start_x, start_y, dir)

                if grid[newx, newy] == "#":
                    break

                start_x = newx
                start_y = newy
                dir = newd

    start_x += 1
    start_y += 1

    p2_result = 1000 * start_y + 4 * start_x + dir
    return p2_result


def main():
    global WIDTH, HEIGHT

    inp = open("input", "r").read().splitlines()

    g, instr = inp[:-2], inp[-1]
    grid = {}
    for y, row in enumerate(g):
        for x, col in enumerate(row):
            if col in ".#":
                grid[x, y] = col

    instr = re.findall("L|R|\d+", instr)

    WIDTH = max(map(len, g))
    HEIGHT = len(g)

    start_x = g[0].index(".")
    start_y = 0

    p1_result = part1(grid, instr, start_x, start_y)
    print(f"Part 1: {p1_result}")

    p2_result = part2(grid, instr, start_x, start_y)
    print(f"Part 2: {p2_result}")


if __name__ == "__main__":
    main()
