cards = input().split()
team_a = {str(i) for i in range(1, 12)}
team_b = {str(i) for i in range(1, 12)}
for card in cards:
    team, player = card.split('-')
    if team == "A":
        team_a.discard(player)
    else:
        team_b.discard(player)
    if len(team_a) < 7 or len(team_b) < 7:
        print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
        print("Game was terminated")
        break
else:
    print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
