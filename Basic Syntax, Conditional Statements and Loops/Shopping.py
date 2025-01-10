# Read the initial budget from the user
budget = int(input("Enter your budget: "))

# Continuously read product prices
while True:
    command = input("Enter the price of the product or 'End': ")
    if command.lower() == "end":
        print("You bought everything needed.")
        break

    price = int(command)
    if price > budget:
        print("You went in overdraft!")
        break

    budget -= price
