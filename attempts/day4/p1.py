# Day 4 Problem 1

import math

X = [line.strip() for line in open('data.in')]

ans = []

for line in X:
    winning_nums = [int(n.strip()) for n in line.split(": ")[1].split(" | ")[0].strip().split(" ") if n != ""]
    card_nums = [int(n.strip()) for n in line.split(": ")[1].split(" | ")[1].strip().split(" ") if n != ""]

    ans.append(math.floor(2 ** (len([x for x in winning_nums if x in card_nums]) - 1)))

print(sum(ans))