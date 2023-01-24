from copy import copy

with open('data.txt', 'r') as f:
    lines = f.readlines()
    values = [l.strip() for l in lines]

gamma, epsilon = '', ''

from copy import copy

oxygen_diagnostics = copy(values)
for column in range(len(values[0])):
    if len(oxygen_diagnostics) == 0:
        break
    line_array = [line[column] for line in oxygen_diagnostics]
    common_bit = '1' if line_array.count('1') >= len(oxygen_diagnostics)/2 \
        else '0'
    oxygen_diagnostics = [entry for entry in oxygen_diagnostics \
                                if entry[column] == common_bit]
oxygen_rating = int(oxygen_diagnostics[0], base=2)
print('oxygen', oxygen_diagnostics[0], oxygen_rating)
    

co2_diagnostics = copy(values)
for i in range(len(values[0])):
    if len(co2_diagnostics) == 1:
        break
    all_entries_at_pos = [entry[i] for entry in co2_diagnostics]
    least_common_bit = '0' if all_entries_at_pos.count('1') >= len(co2_diagnostics)/2 \
                       else '1'
    co2_diagnostics = [entry for entry in co2_diagnostics
                                 if entry[i]==least_common_bit]
co2_rating = int(co2_diagnostics[0], base=2)
print('co2', co2_diagnostics[0], co2_rating)

print('life support rating', oxygen_rating*co2_rating)