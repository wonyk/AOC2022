#!/usr/bin/env python3

import re
from collections import defaultdict
from itertools import product, combinations
from math import inf as INFINITY

Valve = set()
All_Valves = set()
Flow = {}
Dist = defaultdict(lambda: INFINITY)


def get_score(candidate: dict):
    score = 0
    for v, time_left in candidate.items():
        score += Flow[v] * time_left
    return score


def get_candidates(time_left, curr_valve, chosen: dict):

    for next_valve in Valve:
        if next_valve in chosen:
            continue

        new_time_left = time_left - Dist[curr_valve, next_valve] - 1
        if new_time_left < 2:
            continue

        new_opened = chosen | {next_valve: new_time_left}
        yield from get_candidates(new_time_left, next_valve, new_opened)

    yield chosen


def part1():
    time = 30
    best = 0
    chosen = {}

    for candidate in get_candidates(time, "AA", chosen):
        best = max(best, get_score(candidate))

    return best


def part2():

    time = 26
    best = 0
    chosen = {}
    dp = defaultdict(int)

    for candidate in get_candidates(time, "AA", chosen):
        c = frozenset(candidate)
        score = get_score(candidate)

        if score > dp[c]:
            dp[c] = score

    for (human, human_score), (elephant, elephant_score) in combinations(dp.items(), 2):
        if human & elephant:
            continue
        best = max(best, human_score + elephant_score)

    return best


def main():
    global Valve, Flow, Dist

    inp = open("input", "r").read().splitlines()

    regex = "Valve (\w{2}) .*=(\d*); .*valves? (.*)"

    for line in inp:
        v, rate, sinks = re.findall(regex, line)[0]
        All_Valves.add(v)
        if rate != "0":
            Valve.add(v)
            Flow[v] = int(rate)
        for s in sinks.split(", "):
            Dist[v, s] = 1
        Dist[v, v] = 0

    for k, i, j in product(All_Valves, All_Valves, All_Valves):
        Dist[i, j] = min(Dist[i, j], Dist[i, k] + Dist[k, j])

    p1_result = part1()
    print(f"Part 1: {p1_result}")

    p2_result = part2()
    print(f"Part 2: {p2_result}")


if __name__ == "__main__":
    main()
