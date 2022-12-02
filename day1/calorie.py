#!/usr/bin/env python3

inp = open("input", "r").read().splitlines()
sum_list = []

elf_sum = 0

for calorie in inp:
    if calorie == "":
        sum_list.append(elf_sum)
        elf_sum = 0
        continue
    elf_sum += int(calorie)

sum_list.sort(reverse=True)

print(f"Part 1: {sum_list[0]}")

TOP_N = 3

calorie_sum = 0
for i in range(TOP_N):
    calorie_sum += sum_list[i]

print(f"Part 2: {calorie_sum}")
