import numpy as np

with open('adventofcode\day_11\input.txt') as f:
    matrix = np.matrix([[int(val) for val in line.strip()] for line in f.readlines()])


def increasing_value(matrix):
    matrix = matrix + 1
    return matrix

def cut_suroundings(matrix, x, y):
    min_x = x-1 if (x-1 >= 0) else x 
    max_x = x+1 if (x+1 < np.size(matrix[0])) else x 
    min_y = y-1 if (y-1 >= 0) else y
    max_y = y+1 if (y+1 < np.size(matrix[0])) else y
    return matrix[min_x:max_x+1, min_y:max_y+1], min_x, max_x, min_y, max_y


def check_fleshes(matrix):
    count = 0
    for line in range(len(matrix)-1):
        for val in range(matrix[0].size):
            if matrix[line, val] > 9 and matrix[line, val] != -1:
                count = count + 1
                cut_matrix, min_x, max_x, min_y, max_y = cut_suroundings(matrix, line, val)
                cut_matrix = cut_matrix +1
                matrix[min_x:max_x+1, min_y:max_y+1] = cut_matrix
                matrix[line, val] = -1
    print(count)
    return matrix, count


def run_times(matrix, num):
    for _ in range(num):
        matrix = increasing_value(matrix)
        matrix, count = check_fleshes(matrix)
        while count != 0:
             matrix, count = check_fleshes(matrix)
            #  print(matrix)
        matrix = np.where(matrix==-1, 0, matrix)
    return matrix

print(run_times(matrix, 2))

# matrix_cut = increasing_value(cut_suroundings(matrix, 1, 1))
# matrix[0:len(matrix_cut), 0:matrix_cut[0].size] = matrix_cut
# print(matrix)


