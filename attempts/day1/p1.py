# Day 1 Problem 1

X = [line.strip() for line in open('data.in')]

cal = 0

for l in X:
    a = b = 0
    for c in l:
        if c.isdigit():
            a = int(c)
            break
    for c in reversed(l):
        if c.isdigit():
            b = int(c)
            break
    cal += 10 * a + b

print(cal)
