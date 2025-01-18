# Read the number of centuries
centuries = int(input("Enter the number of centuries: "))

# Perform conversions
years = centuries * 100
days = int(years * 365.2422)  # Average days in a year accounting for leap years
hours = days * 24
minutes = hours * 60

# Print the result
print(f"{centuries} centuries = {years} years = {days} days = {hours} hours = {minutes} minutes")
