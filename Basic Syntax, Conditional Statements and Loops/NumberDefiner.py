# Read a floating-point number from the user
number = float(input("Enter a floating-point number: "))

# Check if the number is zero
if number == 0:
    print("zero")
else:
    # Determine if the number is positive or negative
    if number > 0:
        result = "positive"
    else:
        result = "negative"

    # Add "small" or "large" based on the absolute value of the number
    if abs(number) < 1:
        result += " small"
    elif abs(number) > 1_000_000:
        result += " large"

    # Print the result
    print(result)
