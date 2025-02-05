n = int(input())
word = input()
strings = [input() for _ in range(n)]
print(strings)
filtered = [s for s in strings if word in s]
print(filtered)
