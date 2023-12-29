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

seeds_ranges = [(s, s + r) for s, r in zip(seeds[::2], seeds[1::2])]

for s in seeds_ranges:
    tmp = None
    i = [s]

    for a in maps:
        tmp = m[a]
        for sgmt in tmp:
            index = i.pop()
            # 1 2 |    |
            #     |    |  1 2
            if (index[0] < sgmt[0] and index[1] < sgmt[0]) or (
                    index[0] >= sgmt[0] + sgmt[2] and index[1] >= sgmt[0] + sgmt[2]):
                i.append(index)
            # 1   | 2  |
            elif index[0] < sgmt[0] <= index[1] < sgmt[0] + sgmt[2]:
                i.append((index[0], sgmt[0])) if index[0] != sgmt[0] else 0
                i.append((sgmt[1], sgmt[1] + index[1] - sgmt[0]))
                break
            #     | 1  |  2
            elif sgmt[0] <= index[0] < sgmt[0] + sgmt[2] <= index[1]:
                i.append((sgmt[0] + sgmt[2], index[1])) if sgmt[0] + sgmt[2] != index[1] else 0
                i.append((sgmt[1] + index[0] - sgmt[0], sgmt[1] + sgmt[2]))
                break
            #  1  |    |  2
            elif index[0] < sgmt[0] and index[1] >= sgmt[0] + sgmt[2]:
                i.append((index[0], sgmt[0])) if index[0] != sgmt[0] else 0
                i.append((sgmt[0] + sgmt[2], index[1])) if sgmt[0] + sgmt[2] != index[1] else 0
                i.append((sgmt[1], sgmt[1] + sgmt[2]))
                break
            #     | 12 |
            elif index[0] >= sgmt[0] and index[1] < sgmt[0] + sgmt[2]:
                i.append((sgmt[1] + index[0] - sgmt[0], sgmt[1] + index[1] - sgmt[0]))
                break

    for x in i:
        ans.append(x)

print(min(ans))
print(ans)

