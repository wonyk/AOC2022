#!/usr/bin/env python3


def build_tree_view(row, col, inp, is_part1):
    curr_height = inp[row][col]
    top = [curr_height > line[col] for line in inp[:row]]
    bottom = [curr_height > line[col] for line in inp[row + 1 :]]
    left = [curr_height > inp[row][i] for i in range(col)]
    right = [curr_height > inp[row][i] for i in range(col + 1, len(inp[row]))]

    if is_part1:
        return check_visible(top, bottom, left, right)
    else:
        return check_score(top, bottom, left, right)


def check_visible(top, bottom, left, right):
    return all(top) or all(bottom) or all(left) or all(right)


def check_score(top, bottom, left, right):
    top_scene = top[::-1].index(False) + 1 if False in top else len(top)
    bottom_scene = bottom.index(False) + 1 if False in bottom else len(bottom)
    left_scene = left[::-1].index(False) + 1 if False in left else len(left)
    right_scene = right.index(False) + 1 if False in right else len(right)

    return top_scene * bottom_scene * left_scene * right_scene


def part1(inp):
    # Start off with the outer layer
    p1_result = len(inp) * 2 + len(inp[0]) * 2 - 4

    for i in range(1, len(inp) - 1):
        for j in range(1, len(inp[0]) - 1):
            if build_tree_view(i, j, inp, is_part1=True):
                p1_result += 1

    return p1_result


def part2(inp):

    p2_result = 0

    for i in range(1, len(inp) - 1):
        for j in range(1, len(inp[0]) - 1):
            p2_result = max(p2_result, build_tree_view(i, j, inp, is_part1=False))

    return p2_result


def main():
    inp = open("input", "r").read().splitlines()

    for i, row in enumerate(inp):
        inp[i] = [int(char) for char in row]

    p1_result = part1(inp)
    print(f"Part 1: {p1_result}")

    p2_result = part2(inp)
    print(f"Part 2: {p2_result}")


if __name__ == "__main__":
    main()
