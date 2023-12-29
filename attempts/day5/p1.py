# Day 5 Problem 1

X = [line.strip() for line in open('data.in')]

seeds = [int(n.strip()) for n in X[0].split(": ")[1].split(" ")]

c = 3
m = {}
maps = ["seed-to-soil",
        "soil-to-fertilizer",
        "fertilizer-to-water",
        "water-to-light",
        "light-to-temperature",
        "temperature-to-humidity",
        "humidity-to-location"]

for a in maps:
    m[a] = []

for a in maps:
    for line in X[c:]:
        c += 1
        if line == "":
            c += 1
            break

        dest, src, rng = [int(n) for n in line.split(" ")]
        m[a].append([src, dest, rng])

ans = []
for s in seeds:
    tmp = None
    index = s
    for a in maps:
        tmp = m[a]
        for sgmt in tmp:
            if sgmt[0] <= index < sgmt[0] + sgmt[2]:
                index = sgmt[1] + (index - sgmt[0])
                break

    ans.append(index)

print(min(ans))

