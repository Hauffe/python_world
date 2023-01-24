with open('base.txt', 'r') as f:
    lines = f.readlines()
    values = [int(l.strip()) for l in lines]

increase = 0
previous = sum(values[0:3])
for x in range(len(values)):
    val = sum(values[x:x+3])
    if val > previous: increase+=1
    previous = val

print(increase)