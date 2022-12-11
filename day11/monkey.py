#!/usr/bin/env python3

from copy import deepcopy


class Monkey:
    def __init__(self, index):
        self.index = index
        self.items = []
        self.operate = None
        self.number = 0
        self.diviser = 1
        self.m_true = index
        self.m_false = index
        self.inspected = 0
        self.diviser_ring = 1

    def set_items(self, item_str):
        self.items = [int(x) for x in item_str.split(", ")]

    def multiply(self, old):
        return old * self.number

    def add(self, old):
        return old + self.number

    def double(self, old):
        return old * old

    def set_operate_and_num(self, operator, number):
        if operator != "*" and operator != "+":
            print("Error! Operator not supported")
            exit()
        if operator == "*":
            if number == "old":
                self.operate = self.double
                return
            else:
                self.operate = self.multiply
        else:
            self.operate = self.add

        self.number = int(number)

    def set_diviser(self, diviser):
        self.diviser = diviser

    def set_monkey_if_true(self, m_true):
        self.m_true = m_true

    def set_monkey_if_false(self, m_false):
        self.m_false = m_false

    def inspect(self, item_score, reduce_worry=True):
        score = self.operate(item_score)

        if reduce_worry:
            score //= 3
        else:
            score %= self.diviser_ring

        if score % self.diviser == 0:
            next_monkey = self.m_true
        else:
            next_monkey = self.m_false

        self.inspected += 1

        return next_monkey, score

    def clear_items(self):
        self.items = []


def part1(monkey_list):

    NUM_ROUNDS = 20
    for _ in range(NUM_ROUNDS):
        for monkey in monkey_list:
            for item in monkey.items:
                next_monkey, worry_score = monkey.inspect(item, reduce_worry=True)
                monkey_list[next_monkey].items.append(worry_score)
            monkey.clear_items()

    final_scores = [m.inspected for m in monkey_list]
    final_scores.sort(reverse=True)

    return final_scores[0] * final_scores[1]


def part2(monkey_list):

    NUM_ROUNDS = 10000
    for _ in range(NUM_ROUNDS):
        for monkey in monkey_list:
            for item in monkey.items:
                next_monkey, worry_score = monkey.inspect(item, reduce_worry=False)
                monkey_list[next_monkey].items.append(worry_score)
            monkey.clear_items()

    final_scores = [m.inspected for m in monkey_list]
    final_scores.sort(reverse=True)

    return final_scores[0] * final_scores[1]


def main():
    inp = open("input", "r").read().splitlines()

    monkey_list = []
    diviser_ring = 1
    monkey = None

    for line in inp:
        if line.strip() == "":
            continue
        elif line.startswith("Monkey"):
            # remove the colon at the end
            idx = int(line.split()[1][:-1])
            monkey = Monkey(idx)

            monkey_list.append(monkey)
            continue

        cmd, details = line.lstrip().split(": ")

        if cmd.startswith("Starting"):
            monkey.set_items(details)

        elif cmd.startswith("Operation"):
            raw = details.split(" ")
            monkey.set_operate_and_num(raw[3], raw[4])

        elif cmd.startswith("Test"):
            diviser = int(details.split()[-1])
            monkey.set_diviser(diviser)
            diviser_ring *= diviser

        elif "true" in cmd:
            monkey.set_monkey_if_true(int(details.split()[-1]))

        else:
            monkey.set_monkey_if_false(int(details.split()[-1]))

    for m in monkey_list:
        m.diviser_ring = diviser_ring

    p1_result = part1(deepcopy(monkey_list))
    print(f"Part 1: {p1_result}")

    p2_result = part2(deepcopy(monkey_list))
    print(f"Part 2: {p2_result}")


if __name__ == "__main__":
    main()
