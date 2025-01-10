# Read a number to create a star pattern
number = int(input("Enter a number for the star pattern: "))

# Generate the star pattern
for i in range(1, number + 1):
    print("*" * i)
for i in range(number - 1, 0, -1):
    print("*" * i)