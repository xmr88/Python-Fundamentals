# Read the input values
budget = float(input())  # Available budget
price_flour = float(input())  # Price for 1 kg flour

# Calculate the price for other ingredients based on the flour price
price_eggs = price_flour * 0.75  # Price for 1 pack of eggs
price_milk_per_liter = price_flour * 1.25  # Price for 1L of milk
price_milk_per_250ml = price_milk_per_liter * 0.25  # Price for 250ml of milk

# Initialize variables
loafs_made = 0
colored_eggs = 0
money_left = budget

# Start making the bread
while True:
    # Calculate the total cost for one loaf
    cost_of_one_loaf = price_flour + price_eggs + price_milk_per_250ml

    # Check if we have enough money for another loaf
    if money_left >= cost_of_one_loaf:
        # Deduct the cost of one loaf from the money
        money_left -= cost_of_one_loaf
        loafs_made += 1
        colored_eggs += 3  # Add 3 colored eggs for each loaf

        # If it's the 3rd loaf, subtract the lost eggs
        if loafs_made % 3 == 0:
            colored_eggs -= (loafs_made - 2)
    else:
        break  # If we don't have enough money to make another loaf, stop

# Print the result
print(f"You made {loafs_made} loaves of Easter bread! Now you have {colored_eggs} eggs and {money_left:.2f}BGN left.")
