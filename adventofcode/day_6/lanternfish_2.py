

n_days = 256
days = [0] * 9

with open('adventofcode/day_6/input.txt') as f:
    fishes = [int(n) for n in f.readline().split(',')]
    print(fishes)

for day in fishes:
    days[day] += 1

for i in range(n_days):
    today = i % len(days)

    days[(today + 7) % len(days)] += days[today]
    # print(days)

print(sum(days))
