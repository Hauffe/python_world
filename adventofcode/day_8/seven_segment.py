
list = {1:2, 4:4, 7:3, 8:7}

count = 0
with open('adventofcode/day_8/input.txt') as f:
    values = [val.strip() for val in f.readlines()]

for value in values:
    first_segment, seccond_segment = value.split(' | ')
    segment = seccond_segment.split()
    for val in segment:
        if len(val) in list.values():
            count+=1

print(count)