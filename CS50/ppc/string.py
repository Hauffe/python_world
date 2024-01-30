#Strings: ordered, immutable, text representation

multiline_string = """Hello
world"""

print(multiline_string)

sunstring = multiline_string[1:2]
print(sunstring)

# reverse
print(multiline_string[::-1])

# converting list to string
any_string = ''.join(['a', 'b'])
print(any_string)

print("the result is {}".format(any_string))