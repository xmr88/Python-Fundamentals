# Read the input strings
string1 = input()
string2 = input()

# Initialize a list to store already printed strings
printed_strings = []

# Convert the first string to a list so we can modify it
string1_list = list(string1)

# Iterate over each character index of the strings
for i in range(len(string1)):
    # Update the string1 to match string2 character at position i
    string1_list[i] = string2[i]

    # Join the list back into a string
    transformed_string = ''.join(string1_list)

    # Print the transformed string only if it hasn't been printed before
    if transformed_string not in printed_strings:
        print(transformed_string)
        printed_strings.append(transformed_string)
