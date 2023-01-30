# we found the certers, now we can use the same algorithm to run around those points and count until it hits the mountains (num 9)
import math

with open('adventofcode/day_9/input.txt') as f:
    matrix = []
    lines = [list(a.strip()) for a in f.readlines()]
    for line in lines:
        matrix.append([int(val) for val in line])


len_y = len(matrix) #lines
len_x = len(matrix[0]) #columns
values = []

def count_groups(i, j):
    if j < 0 or j >= len(matrix) or i < 0 or i >= len(matrix[0]) or matrix[j][i] == 9 or matrix[j][i] == -1:
        return
    matrix[j][i] = -1
    values[len(values)-1] += 1
    count_groups(i+1, j)
    count_groups(i-1, j)
    count_groups(i, j+1)
    count_groups(i, j-1)


for i in range(0, len_y):
    for j in range(0, len_x):
        values.append(0)
        count_groups(j, i)

print(math.prod(sorted(values, reverse=True)[:3]))