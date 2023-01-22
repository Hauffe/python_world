count = 0
matrix = [[]]

with open('input.txt', 'r') as f:
    lines = f.readlines()
    values = lines[0].split()
    for l in range(2, len(lines)):
        if lines[l].split() == []:
            count +=1
            matrix.append([])
        else:
            matrix[count].append(lines[l].split())
