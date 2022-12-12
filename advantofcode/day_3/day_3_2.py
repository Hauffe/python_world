from copy import copy

with open('data.txt', 'r') as f:
    lines = f.readlines()
    values = [l.strip() for l in lines]

gamma, epsilon = '', ''

from copy import copy

oxygen_diagnostics = copy(values)
