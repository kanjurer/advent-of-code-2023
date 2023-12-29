# Day 4 Problem 2

X = [line.strip() for line in open('data.in')]
num_cards = len(X)


cards_won_at = []
for line in X:
    winning_nums = [int(n.strip()) for n in line.split(": ")[1].split(" | ")[0].strip().split(" ") if n != ""]
    card_nums = [int(n.strip()) for n in line.split(": ")[1].split(" | ")[1].strip().split(" ") if n != ""]
    cards_won_at.append(len([x for x in winning_nums if x in card_nums]))


total_scratches_at = [-1 for _ in range(0, num_cards)]


def number_of_cards_won(card_num):
    n = cards_won_at[card_num]
    s = 0

    while card_num < num_cards - 1:
        if total_scratches_at[card_num + 1] == -1:
            total_scratches_at[card_num + 1] = number_of_cards_won[card_num + 1]

        s += total_scratches_at[card_num + 1] + 1
        card_num += 1

    return s


for n in range(num_cards - 1, -1, -1):
    total_scratches_at[n] = number_of_cards_won(n)

print(sum(total_scratches_at))
