#!/usr/bin/env python3

import numpy as np
import cvxpy as cp
import re


def optimize(blueprint, time):
    (
        _,
        ore_oreR,
        ore_clayR,
        ore_obsidianR,
        clay_obsidianR,
        ore_geodeR,
        obsidian_geodeR,
    ) = blueprint

    costs = np.array(
        [
            [ore_oreR, ore_clayR, ore_obsidianR, ore_geodeR],
            [0, 0, clay_obsidianR, 0],
            [0, 0, 0, obsidian_geodeR],
            [0, 0, 0, 0],
        ]
    )

    old_mineral = cp.Variable(4)
    old_robots = cp.Variable(4)
    old_build = cp.Variable(4, boolean=True)
    constraints = []

    constraints.append(old_mineral == 0)
    constraints.append(old_robots[0] == 1)
    constraints.append(old_robots[1:] == 0)
    constraints.append(old_build == 0)

    for _ in range(1, time + 1):
        mineral = cp.Variable(4)
        robots = cp.Variable(4)
        build = cp.Variable(4, boolean=True)

        constraints.append(robots == old_robots + old_build)
        constraints.append(cp.sum(build) <= 1)
        constraints.append(costs @ build <= old_mineral)
        constraints.append(mineral == old_mineral + robots - (costs @ build))

        old_mineral = mineral
        old_robots = robots
        old_build = build

    obj = cp.Maximize(mineral[3])
    problem = cp.Problem(obj, constraints)
    problem.solve()

    assert problem.status == cp.OPTIMAL
    return problem.value


def main():
    inp = open("input", "r").read().splitlines()

    blueprints = []
    for line in inp:
        blueprints.append(tuple(map(int, re.findall("\d+", line))))

    p1_result = 0
    for blueprint in blueprints:
        p1_result += optimize(blueprint, time=24) * blueprint[0]
    print(f"Part 1: {p1_result}")

    p2_result = 1
    for blueprint in blueprints[:3]:
        p2_result *= optimize(blueprint, time=32)
    print(f"Part 2: {p2_result}")


if __name__ == "__main__":
    main()
