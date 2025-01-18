# Read the amount in British pounds
pounds = int(input("Enter amount in British pounds: "))

# Convert pounds to US dollars
dollars = pounds * 1.31

# Print the result formatted to 3 decimal places
print(f"{dollars:.3f}")
