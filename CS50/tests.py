from itertools import permutations
nums = [3, 4, 5, 1, 2]

def solution(nums):
    count = 0
    t = len(nums)
    for _ in range(t-1):
        nums = [x for x in nums if x != nums[0]] + [nums[0]]
        count +=1
        if nums == sorted(nums):
            return count
    return -1



def undo(history, result):
    operation = history[-1][0]
    if operation == "INSERT":
        result = result + history[-1][1]
        history.pop()
    if operation == "DELETE":
        result = result.replace(history[-1][1], "")
        history.pop()
    return history, result



def solution(operations):
    result = ""
    history = []
    for ops in operations:
        if ops == "DELETE" and len(result)>0:
            history.append(["INSERT", result[-1]])
            result = result[:-1]
        elif ops == "UNDO" and len(history) > 0:
            history, result = undo(history, result)
        elif "INSERT" in ops:
            command, text = ops.split(" ")
            result = result + text
            history.append(["DELETE", text])
    return result
        


# There are 8 ways to make a 3×3 magic square.

# n=4
# result = 1
# for i in range(n):
#     result *=(n-i)
# print(result)


def solve(x):
    position_count = 0
    result = 0
    l = list(permutations(range(1, len(x)+1)))
    # for permutation in l:
    #     temp = []
    #     temp = [x for x in permutation]
    #     position_count +=1
    #     for position in range(len(permutation)):
    #         if x[position] == 0:
    #             temp[position] = 0
    #     if temp == x:
    #         result += position_count
    print(l)
    


solve([22, 15, 14, 0, 5, 0, 9, 12, 0, 0, 0, 0, 0, 0, 0, 3, 17, 20, 0, 0, 0, 0, 0, 0, 23])
# operations = ["DELETE", "DELETE", "INSERT Nothing", 
#  "INSERT is", 
#  "INSERT Permanent", 
#  "UNDO", 
#  "UNDO", 
#  "UNDO",
#  "UNDO"]

# solution(operations)