n = int(input())
numbers = [int(input()) for _ in range(n)]
command = input()
if command == "even":
    filtered = [num for num in numbers if num % 2 == 0]
elif command == "odd":
    filtered = [num for num in numbers if num % 2 != 0]
elif command == "positive":
    filtered = [num for num in numbers if num >= 0]
elif command == "negative":
    filtered = [num for num in numbers if num < 0]
print(filtered)
