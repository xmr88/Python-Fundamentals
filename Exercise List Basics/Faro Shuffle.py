cards = input().split()
shuffles = int(input())
for _ in range(shuffles):
    mid = len(cards) // 2
    shuffled = []
    for i in range(mid):
        shuffled.append(cards[i])
        shuffled.append(cards[i + mid])
    cards = shuffled
print(cards)
