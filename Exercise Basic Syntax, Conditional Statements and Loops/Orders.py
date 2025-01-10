# Function to calculate the price for each coffee order
def calculate_order_price(price_per_capsule, days, capsules_per_day):
    return price_per_capsule * days * capsules_per_day

# Initialize total price accumulator
total_price = 0.0

# Get the number of orders
N = int(input("Enter the number of orders: "))

# Process each order
for _ in range(N):
    # Read the input values for each order
    price_per_capsule = float(input("Enter the price per capsule: "))
    days = int(input("Enter the number of days: "))
    capsules_per_day = int(input("Enter the capsules needed per day: "))

    # Check if the input values are in the correct range
    if 0.01 <= price_per_capsule <= 100.00 and 1 <= days <= 31 and 1 <= capsules_per_day <= 2000:
        # Calculate the price for the current order
        order_price = calculate_order_price(price_per_capsule, days, capsules_per_day)
        # Print the price for the current order
        print(f"The price for the coffee is: ${order_price:.2f}")
        # Add the order price to the total price
        total_price += order_price

# Print the total price
print(f"Total: ${total_price:.2f}")
