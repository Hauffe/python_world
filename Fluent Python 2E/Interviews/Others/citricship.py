import hashlib

# - Start with the string "CitricSheep"

string = "CitricSheep"
print(len(string))

# - Use the ASCII values of each character in the string and generate a list of these values.

lst = [ord(c) for c in list(string)]
print(lst)

# - Multiply each value in the list by the number of characters in the string.

mult = [i*len(string) for i in lst]
print(mult)

# - Find the sum of all numbers in the resulting list.

total = sum(mult)
print(total)

# - Use this sum to generate a SHA256 hash.
# - Convert this hash to a hexadecimal string.

### There is two ways of doing it:

#This one gets a hash value from the int directly by using the length
byte_representation = total.to_bytes((total.bit_length() + 7) // 9, 'big')
print(hashlib.sha256(byte_representation).hexdigest())
# 82265beba8ec587f82f55c774cdebef6b313d388a418482ecad41bcfa84aaa73

#This one converts into a String and can be modified before encoding it, the resuts may differ.
sha256_hash = hashlib.sha256(str(total).encode('utf-8')).hexdigest()
print(sha256_hash)
# 44aad44806272b73f17ba4027a0645985b0851ea5723d4d20c46ae14d6be68b4

# output
# 11
# [67, 105, 116, 114, 105, 99, 83, 104, 101, 101, 112]
# [737, 1155, 1276, 1254, 1155, 1089, 913, 1144, 1111, 1111, 1232]
# 12177
# 82265beba8ec587f82f55c774cdebef6b313d388a418482ecad41bcfa84aaa73
# 44aad44806272b73f17ba4027a0645985b0851ea5723d4d20c46ae14d6be68b4