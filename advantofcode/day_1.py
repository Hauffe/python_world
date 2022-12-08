with open('base.txt', 'r') as f:
    lines = f.readlines()
    values = [int(l.strip()) for l in lines]

increase = 0
previous = values[0]
for val in values[1:]:
    if val > previous: increase+=1
    previous = val

print(increase)
