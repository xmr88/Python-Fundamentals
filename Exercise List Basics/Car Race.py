times = list(map(int, input().split()))
middle = len(times) // 2
left_time = sum(times[:middle]) - sum(times[i] * 0.2 for i in range(middle) if times[i] == 0)
right_time = sum(times[:middle:-1]) - sum(times[-i] * 0.2 for i in range(1, middle + 1) if times[-i] == 0)
if left_time < right_time:
    print(f"The winner is left with total time: {left_time:.1f}")
else:
    print(f"The winner is right with total time: {right_time:.1f}")
