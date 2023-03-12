
open_close_chars = {"{":"}", "(":")", "<":">", "[":"]"}
points = {")":3, "]":57, "}":1197, ">":25137}
result = 0

with open('adventofcode/day_10/input.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]


def verify_characteres(line):
    verifying_arr = []
    for character in line:
        if character in open_close_chars.keys():
            verifying_arr.extend(character)
        else:
            if open_close_chars.get(verifying_arr[-1]) == character:
                verifying_arr.pop()
            else:
                print(f'expected {open_close_chars.get(verifying_arr[-1])}, but found ')
                print(verifying_arr)
                return character
    return True


for line in lines:
    character = verify_characteres(line)
    if character != True:
        print(character)
        result+= points.get(character)
        print(result)
