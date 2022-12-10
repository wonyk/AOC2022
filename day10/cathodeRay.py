#!/usr/bin/env python3


def part1(inp):
    p1_result = 0

    cycle = 1
    X = 1
    TRACK_CYCLES = [20, 60, 100, 140, 180, 220]

    for instruction in inp:
        if "noop" in instruction:
            cycle += 1
        else:
            number = int(instruction.split()[1])
            cycle += 2
            X += number

        if cycle > TRACK_CYCLES[0]:
            p1_result += TRACK_CYCLES.pop(0) * (X - number)
            if len(TRACK_CYCLES) == 0:
                break
        elif cycle == TRACK_CYCLES[0]:
            p1_result += TRACK_CYCLES.pop(0) * X
            if len(TRACK_CYCLES) == 0:
                break

    return p1_result


def part2(inp):

    cycle = 0
    X = 1
    canvas = [["" for _ in range(40)] for _ in range(6)]

    for instruction in inp:
        if "noop" in instruction:
            canvas = check_and_draw(canvas, cycle, X)
            cycle += 1
        else:
            number = int(instruction.split()[1])
            for _ in range(2):
                canvas = check_and_draw(canvas, cycle, X)
                cycle += 1
            X += number

    return canvas


def check_and_draw(canvas, cycle, X):
    row = cycle // 40
    col = cycle % 40

    if X - 1 <= col <= X + 1:
        canvas[row][col] = "#"
    else:
        canvas[row][col] = "."

    return canvas


def main():
    inp = open("input", "r").read().splitlines()

    p1_result = part1(inp)
    print(f"Part 1: {p1_result}")

    p2_result = part2(inp)
    for i in range(6):
        print("".join(p2_result[i]))


if __name__ == "__main__":
    main()
