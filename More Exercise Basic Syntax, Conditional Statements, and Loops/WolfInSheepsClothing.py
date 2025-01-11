# Read the input string
queue = input("Enter the queue (e.g., sheep, sheep, wolf, sheep): ").split(", ")

# Find the position of the wolf in the queue
wolf_position = queue.index("wolf")

# Determine the response
if wolf_position == len(queue) - 1:
    print("Please go away and stop eating my sheep")
else:
    sheep_at_risk = len(queue) - wolf_position - 1
    print(f"Oi! Sheep number {sheep_at_risk}! You are about to be eaten by a wolf!")
