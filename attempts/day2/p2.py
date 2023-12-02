# Day 2 Problem 2

import re

X = [line.strip() for line in open('data.in')]
c = 0
ans = []

for l in X:
    tmp = [0, 0, 0]

    for s in l.split(': ')[1].split(';'):
        for ball in s.split(','):
            if ball.find('red') != -1:
                tmp[0] = max(int(re.findall(r'\d+', ball)[0]), tmp[0])
            if ball.find('green') != -1:
                tmp[1] = max(int(re.findall(r'\d+', ball)[0]), tmp[1])
            if ball.find('blue') != -1:
                tmp[2] = max(int(re.findall(r'\d+', ball)[0]), tmp[2])

    ans.append(tmp[0] * tmp[1] * tmp[2])

print(sum(ans))
