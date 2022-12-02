#!/usr/bin/env python3

inp = open("input", "r").read().splitlines()

opponent_hand = {"A": "R", "B": "P", "C": "S"}

my_hand = {"X": "R", "Y": "P", "Z": "S"}

# The key wins the value
win_guide = {"R": "S", "S": "P", "P": "R"}
lose_guide = {"S": "R", "P": "S", "R": "P"}

play_score = {"R": 1, "P": 2, "S": 3}
status_score = {"W": 6, "D": 3, "L": 0}

p1_total_score = 0
for strategy in inp:
    opp, recomm = strategy.split()
    opp_choice = opponent_hand[opp]
    recomm_choice = my_hand[recomm]

    p1_total_score += play_score[recomm_choice]

    status = "L"

    # if win
    if win_guide[recomm_choice] == opp_choice:
        status = "W"
    # if draw
    elif recomm_choice == opp_choice:
        status = "D"

    p1_total_score += status_score[status]

print(f"Part 1: {p1_total_score}")

# Part 2:
p2_total_score = 0
for strategy in inp:
    opp, recomm = strategy.split()
    opp_choice = opponent_hand[opp]

    my_choice = ""
    # Need to lose
    if recomm == "X":
        my_choice = win_guide[opp_choice]
        p2_total_score += status_score["L"]
    # Need to draw
    elif recomm == "Y":
        my_choice = opp_choice
        p2_total_score += status_score["D"]
    # Need to win
    else:
        my_choice = lose_guide[opp_choice]
        p2_total_score += status_score["W"]

    p2_total_score += play_score[my_choice]

print(f"Part 2: {p2_total_score}")
