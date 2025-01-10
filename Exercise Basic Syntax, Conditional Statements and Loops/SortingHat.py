while True:
    # Read the student's name
    name = input()

    # Check if the name is "Welcome!" or "Voldemort"
    if name == "Welcome!":
        print("Welcome to Hogwarts.")
        break
    elif name == "Voldemort":
        print("You must not speak of that name!")
        break

    # Sort the student based on the length of their name
    if len(name) < 5:
        print(f"{name} goes to Gryffindor.")
    elif len(name) == 5:
        print(f"{name} goes to Slytherin.")
    elif len(name) == 6:
        print(f"{name} goes to Ravenclaw.")
    else:
        print(f"{name} goes to Hufflepuff.")
