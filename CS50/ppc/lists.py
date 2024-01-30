lst = ["cherry", "banana", "lemon"]

print(lst)

lst2 = [lst, 2, 5, "anything"]

print(lst2[-1])

if "banana" in lst2[0]:
    print("yes")

# add remove elements
lst.pop()

print(lst2)

lst.reverse()
lst.sort()

print(lst)

newlst = [0] * 5
print(newlst)

newlst2 = newlst + [1]
print(newlst2)

newlst3 = [i for i in range(1, 10)]
print(newlst3)

# slice
print( newlst3[1:5])
print( newlst3[2:])
print( newlst3[:5])
print( newlst3[::2])
print( newlst3[::-1]) # reverse list


# copy list
lst2 = lst.copy()
lst3 = lst[:]