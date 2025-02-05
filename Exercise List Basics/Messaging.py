numbers = list(map(int, input().split()))
text = list(input())
message = ""
for num in numbers:
    index = sum(map(int, str(num))) % len(text)
    message += text.pop(index)
print(message)
