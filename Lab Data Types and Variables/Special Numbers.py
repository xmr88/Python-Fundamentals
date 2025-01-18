# Read the input
n = int(input("Enter an integer n: "))

# Loop through all numbers from 1 to n
for num in range(1, n + 1):
    # Calculate the sum of the digits
    sum_of_digits = sum(int(digit) for digit in str(num))

    # Check if the sum of digits is special (5, 7, or 11)
    is_special = sum_of_digits in [5, 7, 11]

    # Print the result
    print(f"{num} -> {is_special}")
