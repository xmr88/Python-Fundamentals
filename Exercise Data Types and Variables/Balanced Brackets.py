n = int(input())
balance = 0
valid = True
for _ in range(n):
    line = input()
    if line == "(":
        if balance == 1:
            valid = False
            break
        balance = 1
    elif line == ")":
        if balance == 0:
            valid = False
            break
        balance = 0
print("BALANCED" if valid and balance == 0 else "UNBALANCED")
