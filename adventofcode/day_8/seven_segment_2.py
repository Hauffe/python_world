# 1 - the only 2 elements
# 2 - 2 elements of 4 and len = 5
# 3 - has all elements of 7 and len = 5
# 4 - the only 4 elements
# 5 - 3 elements of 4 and len = 5
# 6 - 2 elements of 7 and len = 6
# 7 - the only 3 elements
# 8 - the only 7 elements
# 9 - has all elements of 4 and len = 6
# 0 - has elements of 7 amd len 6

elements = {0:'', 1:'', 2:'', 3:'', 4:'', 5:'', 6:'', 7:'', 8:'', 9:''}
count = 0
total = 0
with open('adventofcode/day_8/input.txt') as f:
    values = [val.strip() for val in f.readlines()]

# 2 - 2 elements of 4 and len = 5
# 3 - has all elements of 7 and len = 5
# 5 - 3 elements of 4 and len = 5
def len_five_elements(list_sent):
    for num in list_sent:
        total = sum([a == b for a in list(num) for b in list(elements[4])])
        if total == 2:
            elements[2] = num
        elif sum([a == b for a in list(num) for b in list(elements[7])]) == 3:
            elements[3] = num
        elif total == 3:
            elements[5] = num

# 6 - 2 elements of 7 and len = 6
# 9 - has all elements of 4 and len = 6
# 0 - has all elements of 7 amd len 6
def len_six_elements(list_sent):
    for num in list_sent:
        total = sum([a == b for a in list(num) for b in list(elements[7])])
        if sum([a == b for a in list(num) for b in list(elements[4])]) == 4:
            elements[9] = num
        elif total == 3:
            elements[0] = num
        elif total == 2:
            elements[6] = num

def translate(list_sent):
    val = ''
    for num in list_sent:
        val += str([i for i in elements if sorted(elements[i])==sorted(num)][0])
    print(list_sent)
    print(val)
    return int(val)

for value in values:
    first_segment, second_segment = value.split(' | ')
    first = first_segment.split()
    second = second_segment.split()
    first.sort(key=len)
    elements[1]= first[0]
    elements[7]= first[1]
    elements[4]= first[2]
    elements[8]= first[9]
    len_five_elements(first[3:6])
    len_six_elements(first[6:9])
    total += translate(second)
print(total)


