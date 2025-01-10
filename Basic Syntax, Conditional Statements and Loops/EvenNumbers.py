# Read the number of lines (n) from the user
n = int(input("Enter the number of lines: "))

# Initialize a flag to check if all numbers are even
all_even = True

# Process each line
for _ in range(n):
    number = int(input("Enter an integer: "))
    if number % 2 != 0:
        print(f"{number} is odd!")
        all_even = False
        break

# If all numbers are even, print the appropriate message
if all_even:
    print("All numbers are even.")
