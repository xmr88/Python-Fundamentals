def chat_response(num):
    if num == 88:
        return "Hello"
    elif num == 86:
        return "How are you?"
    elif num < 88:
        return "GREAT!"
    else:
        return "Bye."

# Get the number of messages
n = int(input("Enter the number of messages: "))

# Process each message number and print the corresponding response
for _ in range(n):
    message_number = int(input())
    print(chat_response(message_number))
