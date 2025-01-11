# Function to count specific words in a string
def count_beach_words(input_string):
    # Define the words to count
    words = ["sand", "water", "fish", "sun"]
    # Count occurrences of each word (case insensitive)
    return sum(input_string.lower().count(word) for word in words)

# Process user input dynamically
while True:
    input_string = input("Enter a string (or type 'END' to stop): ")
    if input_string.upper() == "END":
        break
    count = count_beach_words(input_string)
    print(f"Count of beach words: {count}")
