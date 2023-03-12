
open_close_chars = {"{":"}", "(":")", "<":">", "[":"]"}
points = {")":3, "]":57, "}":1197, ">":25137}
points_incomplete = {")":1, "]":2, "}":3, ">":4}
scores = []

with open('adventofcode/day_10/input.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]


def verify_characteres(line) -> any:
    verifying_arr = []
    for character in line:
        if character in open_close_chars.keys():
            verifying_arr.append(character)
        else:
            if open_close_chars.get(verifying_arr[-1]) == character:
                verifying_arr.pop()
            else:
                return False
    return verifying_arr

def count_incomplete(line) -> int:
    score = 0
    line.reverse()
    for open_char in line:
        close_char = open_close_chars.get(open_char)
        score = (score*5)+points_incomplete.get(close_char)
    return score


for line in lines:
    incomplete = verify_characteres(line)
    if incomplete:
        scores.append(count_incomplete(incomplete))
    scores.sort()
    middle = (len(scores)-1)//2
print(scores[middle])