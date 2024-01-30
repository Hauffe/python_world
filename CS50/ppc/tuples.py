tp = ("anything",)
print(type(tp))

tp = tuple(["max", 28, "Bostom"])
print(tp[1])

# tp[0] = "Tim" # error bc it is imutable

my_tuple = (1,2,3,4)
i1, *i2, i3 = my_tuple

print(i1)
print(i2)
print(i3)


#touples are more eficient and lists

#the rest is all the same.