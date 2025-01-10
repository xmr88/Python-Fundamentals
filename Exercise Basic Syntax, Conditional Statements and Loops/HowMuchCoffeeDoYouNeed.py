# Initialize the total coffee count
total_coffees = 0

while True:
    # Get the event input
    event = input()

    # Check if the command is "END", if so, stop the loop
    if event == "END":
        break

    # Check if the event is valid
    if event.lower() in ["coding", "dog", "cat", "movie"]:
        # Determine the number of coffees based on the case of the event
        if event.islower():
            total_coffees += 1
        else:
            total_coffees += 2

# Check if the total coffee count exceeds 5
if total_coffees > 5:
    print("You need extra sleep")
else:
    print(total_coffees)
