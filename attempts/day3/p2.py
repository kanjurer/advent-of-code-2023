import re

X = [line.strip() for line in open('data.in')]

ans = []
X = [None, *X, None]

for prev, line, nxt in zip(X, X[1:], X[2:]):
    for match in re.finditer(r'\*', line):
        c = 0
        val = 1
        isAdd = False

        for m in re.finditer(r'\d+', line):
            if m.start() == match.end():
                c = c + 1
                val = val * int(m.group())
            if m.end() == match.start():
                c = c + 1
                val = val * int(m.group())

        if prev:
            for m in re.finditer(r'\d+', prev):
                if match.start() >= m.start() - 1 and match.end() <= m.end() + 1:
                    c = c + 1
                    val = val * int(m.group())
        if nxt:
            for m in re.finditer(r'\d+', nxt):
                if match.start() >= m.start() - 1 and match.end() <= m.end() + 1:
                    c = c + 1
                    val = val * int(m.group())
        if c == 2:
            ans.append(val)


print(sum(ans))
