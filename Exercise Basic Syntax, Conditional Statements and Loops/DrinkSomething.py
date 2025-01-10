def drink_by_age(age):
    if age <= 14:
        return "Toddy"
    elif age <= 18:
        return "Coke"
    elif age <= 21:
        return "Beer"
    else:
        return "Whisky"

# Get the age from the user
age = int(input("Enter your age: "))

# Call the function and print the result
print(f"You drink {drink_by_age(age)}.")
