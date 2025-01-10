# Continuously read floating-point numbers from the user
while True:
    number = float(input("Enter a floating-point number: "))
    if 1 <= number <= 100:
        print(f"The number {number} is between 1 and 100.")
        break
