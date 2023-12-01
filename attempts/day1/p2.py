# Day 1 Problem 2

X = [line.strip() for line in open('data.in')]

m = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

cal = 0

for l in X:
    a = b = 0

    alphaIndex = [l.find(k) for k in m]
    numIndex = [l.find(str(m[k])) for k in m]

    x = [i for i in alphaIndex if i >= 0]
    y = [i for i in numIndex if i >= 0]
    minAlphaIndex = min(x) if x else 1000000000000000000
    minNumIndex = min(y) if y else 1000000000000000000
    a = alphaIndex.index(minAlphaIndex)+1 if minAlphaIndex < minNumIndex else int(l[minNumIndex])

    alphaIndex = [l.rfind(k) for k in m]
    numIndex = [l.rfind(str(m[k])) for k in m]

    x = [i for i in alphaIndex if i >= 0]
    y = [i for i in numIndex if i >= 0]

    maxAlphaIndex = max(x) if x else -1
    maxNumIndex = max(y) if y else -1

    b = alphaIndex.index(maxAlphaIndex)+1 if maxAlphaIndex > maxNumIndex else int(l[maxNumIndex])

    cal += 10 * a + b

print(cal)
