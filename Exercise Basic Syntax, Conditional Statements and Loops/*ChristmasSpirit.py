# Read the input values
quantity = int(input())  # Number of decorations to buy each time
days = int(input())  # Number of days left until Christmas

# Initialize variables for cost and spirit
total_cost = 0
total_spirit = 0

# Loop through each day and calculate cost and spirit
for day in range(1, days + 1):
    # Every second day - Buy Ornament Sets
    if day % 2 == 0:
        total_cost += 2 * quantity  # 2$ per piece for Ornament Sets
        total_spirit += 5  # 5 spirit points for Ornament Sets

    # Every third day - Buy Tree Skirts and Tree Garlands
    if day % 3 == 0:
        total_cost += 5 * quantity  # 5$ per piece for Tree Skirts
        total_spirit += 3  # 3 spirit points for Tree Skirts
        total_cost += 3 * quantity  # 3$ per piece for Tree Garlands
        total_spirit += 10  # 10 spirit points for Tree Garlands

    # Every fifth day - Buy Tree Lights
    if day % 5 == 0:
        total_cost += 15 * quantity  # 15$ per piece for Tree Lights
        total_spirit += 17  # 17 spirit points for Tree Lights

        # If both Tree Lights and Tree Garlands are bought on the same day, additional 30 spirit points
        if day % 3 == 0:
            total_spirit += 30

    # Every tenth day - Cat ruins decorations
    if day % 10 == 0:
        total_spirit -= 20  # Lose 20 points of spirit due to cat
        # Second shopping for Tree Skirt, Tree Garlands, and Tree Lights (no additional spirit points)
        total_cost += 5 * quantity  # Tree Skirt
        total_cost += 3 * quantity  # Tree Garlands
        total_cost += 15 * quantity  # Tree Lights

    # Every eleventh day - Increase the quantity of decorations to be bought
    if day % 11 == 0:
        quantity += 2

    # Last day (if the last day is a tenth day, cat ruins even more)
    if day == days and day % 10 == 0:
        total_spirit -= 30  # Lose 30 points due to the last day cat damage

# Output the results
print(f"Total cost: {total_cost}")
print(f"Total spirit: {total_spirit}")
