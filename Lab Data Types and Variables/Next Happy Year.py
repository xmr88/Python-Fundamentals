# Read the input year
year = int(input("Enter the year: "))

# Function to check if a year has all distinct digits
def is_happy_year(year):
    return len(set(str(year))) == len(str(year))

# Find the next happy year
while True:
    year += 1
    if is_happy_year(year):
        print(year)
        break
