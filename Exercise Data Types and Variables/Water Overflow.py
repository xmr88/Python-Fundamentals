n = int(input())
tank_capacity = 255
total_liters = 0
for _ in range(n):
    liters = int(input())
    if total_liters + liters > tank_capacity:
        print("Insufficient capacity!")
    else:
        total_liters += liters
print(total_liters)
