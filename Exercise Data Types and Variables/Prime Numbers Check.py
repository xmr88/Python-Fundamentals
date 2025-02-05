num = int(input())
if num > 1:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print(False)
            break
    else:
        print(True)
else:
    print(False)
