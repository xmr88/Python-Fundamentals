numbers = list(map(int, input().split(', ')))
non_zeros = [num for num in numbers if num != 0]
zeros = [0] * numbers.count(0)
print(non_zeros + zeros)
