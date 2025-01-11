# Read the input string
input_string = input("Enter a string: ")

# Find indices of all capital letters
capital_indices = [index for index, char in enumerate(input_string) if char.isupper()]

# Print the list of indices
print(capital_indices)
