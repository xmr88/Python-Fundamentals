numbers = list(map(int, input().split(', ')))
beggars_count = int(input())
result = [0] * beggars_count
for i in range(len(numbers)):
    result[i % beggars_count] += numbers[i]
print(result)
