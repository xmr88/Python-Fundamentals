while True:
    # Get the input string
    string = input()

    # Check if the string is "End", if so, stop the loop
    if string == "End":
        break

    # Skip the string "SoftUni"
    if string == "SoftUni":
        continue

    # Print each character in the string repeated twice
    print(''.join([char * 2 for char in string]))
