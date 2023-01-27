with open('adventofcode/day_9/input.txt') as f:
    matrix = []
    lines = [list(a.strip()) for a in f.readlines()]
    for line in lines:
        matrix.append([int(val) for val in line])


len_y = len(matrix) #lines
len_x = len(matrix[0]) #columns
values = []


for line in range(len_y):
    for val in range(len_x):
        min_y = line-1 if (line-1) >= 0 else line
        max_y = line+1 if (line+1) <= len_y else line
        min_x = val-1 if (val-1) >= 0 else val
        max_x = val+1 if (val+1) <= len_x else val
        neighbours = [
                        inner_val > matrix[line][val] 
                        for inner_line in matrix[min_y:max_y+1]
                        for inner_val in inner_line[min_x:max_x+1]
                    ]
        if sum(neighbours) == len(neighbours)-1:
            values.append(matrix[line][val]+1)
        # print(f'neighbours of {matrix[line][val]}: {neighbours}')

print(sum(values))


