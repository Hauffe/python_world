import numpy as np
import math as m

with open('adventofcode/day_7/input.txt') as f:
    values = [int(val) for val in f.readline().split(',')]


min_sum = 1e10
# for val_1 in values:
#        tmp_sum = sum([abs(val_1*(val_1+1) - val) for val in values])
#        if tmp_sum < min_val:
#              min_val = tmp_sum

min_val = min(values)
max_val = max(values)

for val_1 in range(min_val, max_val):
    tmp_sum = 0
    for val in values:
        casas = abs(val_1 - val)
        tmp_sum += sum([a for a in range(1, casas+1)])
    if tmp_sum < min_sum:
            min_sum = tmp_sum
    print(f'Min for {val_1} is {min_sum}')

print(min_sum)