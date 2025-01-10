# Get the divisor and boundary from the user
divisor = int(input("Enter the divisor: "))
boundary = int(input("Enter the boundary: "))

# Find the largest integer N that is divisible by the divisor and <= boundary
largest_N = boundary // divisor * divisor

# Print the result
print(largest_N)
