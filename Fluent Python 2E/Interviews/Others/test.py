import hashlib

# Start with the string
original_string = "CitricSheep"

# Use the ASCII values of each character and generate a list
ascii_values_list = [ord(char) for char in original_string]

# Multiply each value in the list by the number of characters in the string
multiplied_values = [value * len(original_string) for value in ascii_values_list]

# Find the sum of all numbers in the resulting list
sum_of_values = sum(multiplied_values)

# Use the sum to generate a SHA256 hash
sha256_hash = hashlib.sha256(str(sum_of_values).encode('utf-8')).hexdigest()

print(f"Original String: {original_string}")
print(f"ASCII Values List: {ascii_values_list}")
print(f"Multiplied Values: {multiplied_values}")
print(f"Sum of Multiplied Values: {sum_of_values}")
print(f"SHA256 Hash (hex): {sha256_hash}")