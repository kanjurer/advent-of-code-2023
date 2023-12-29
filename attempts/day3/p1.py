# Day 3 Problem 1

import re

X = [line.strip() for line in open('data.in')]

ans = []
X = [None, *X, None]
for prev, line, nxt in zip(X, X[1:], X[2:]):
    for match in re.finditer(r'\d+', line):
        isAdd = False
        # left and right is OK
        if (
                (True if match.start() == 0 else not bool(re.compile(r"[^0-9.]").search(line[match.start() - 1]))) and
                (True if match.end() == len(line) else not bool(re.compile(r"[^0-9.]").search(line[match.end()])))
        ):
            # up and down is OK
            if prev:
                for m in re.finditer(r"[^0-9.]", prev):
                    if m.start() >= match.start() - 1 and m.end() <= match.end() + 1:
                        isAdd = True
                        break

            if nxt:
                for m in re.finditer(r"[^0-9.]", nxt):
                    if m.start() >= match.start() - 1 and m.end() <= match.end() + 1:
                        isAdd = True
                        break

            if isAdd:
                ans.append(int(match.group()))
        else:
            ans.append(int(match.group()))

print(sum(ans))
