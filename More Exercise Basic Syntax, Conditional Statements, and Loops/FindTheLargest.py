# Read the input number as a string
number = input()

# Sort the digits in descending order
sorted_digits = sorted(number, reverse=True)

# Join the sorted digits to form the largest number
largest_number = ''.join(sorted_digits)

# Print the largest number
print(largest_number)
