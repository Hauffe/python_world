# read the file - ok
# no diagonals for now 
#
import numpy as np

max_x = 0
max_y = 0

def critical_points(grid, x1, x2, y1, y2):
    if x1 == x2:
        for y in range(min(y1, y2), max(y1, y2)+1):
            grid[y, x1] += 1
        return
    if y1 == y2:
        for x in range(min(x1, x2), max(x1, x2)+1):
            grid[y1, x] +=1
        return
    line_length = abs(x1-x2)+1
    step_x = 1 if x2-x1 > 0 else -1
    step_y = 1 if y2-y1 > 0 else -1
    for i in range(line_length):
        new_x = x1 + i*step_x
        new_y = y1 + i*step_y
        grid[new_y, new_x] += 1



with open('advantofcode/day_5/input.txt') as f:
    lines = [entry.strip() for entry in f.readlines()]
    for l in lines:
        x1, y1, x2, y2 = [int(val) for val in l.replace(' -> ', ',').split(',')]
        max_x = max(max_x, x1, x2)
        max_y = max(max_y, y1, y2)

    print('max x', max_x, 'max y', max_y)
    grid = np.zeros((max_y+1, max_x+1), dtype=int)

for l in lines:
    x1, y1, x2, y2 = [int(val) for val in l.replace(' -> ', ',').split(',')]
    critical_points(grid, x1, x2, y1, y2)

print('score', (grid >= 2).sum())
