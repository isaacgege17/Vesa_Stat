print("TEAM ROSTER")
players_no = int(input("How many players? "))
players = []
for i in range(players_no):
    player_name = input("Player Name: ")
    players.append(player_name)
print("PLAYERS")
for i in range(len(players)):
    print(i + 1 , players[i])