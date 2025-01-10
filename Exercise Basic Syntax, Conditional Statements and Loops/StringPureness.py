# Get the number of strings
n = int(input("Enter the number of strings: "))

# Process each string
for _ in range(n):
    # Read the string
    string = input()

    # Check if the string contains any of the forbidden characters
    if "," in string or "." in string or "_" in string:
        print(f"{string} is not pure!")
    else:
        print(f"{string} is pure.")
