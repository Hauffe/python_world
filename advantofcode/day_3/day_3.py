with open('data.txt', 'r') as f:
    lines = f.readlines()
    values = [l.strip() for l in lines]

gamma, epsilon = '', ''

for column in range(len(values[0])):
    line_array = [line[column] for line in values]
    if line_array.count('0') > line_array.count('1'):
        gamma += '0'
        epsilon += '1'
    else:
        gamma += '1'
        epsilon += '0'
print(int(gamma, base=2) * int(epsilon, base=2))






