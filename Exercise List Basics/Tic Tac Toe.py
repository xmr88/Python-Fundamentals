board = [list(map(int, input().split())) for _ in range(3)]
for i in range(3):
    if board[i][0] == board[i][1] == board[i][2] != 0:
        print(f"{'First' if board[i][0] == 1 else 'Second'} player won")
        break
    if board[0][i] == board[1][i] == board[2][i] != 0:
        print(f"{'First' if board[0][i] == 1 else 'Second'} player won")
        break
else:
    if board[0][0] == board[1][1] == board[2][2] != 0 or board[0][2] == board[1][1] == board[2][0] != 0:
        print(f"{'First' if board[1][1] == 1 else 'Second'} player won")
    else:
        print("Draw!")
