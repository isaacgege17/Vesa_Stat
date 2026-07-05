num_players = int(input("How many players: "))
total_points = 0
for i in range(num_players):
    player_name = input("Enter player name: ")
    player_points = int(input("Enter player points: "))
    total_points += player_points
print("Total Team Points: " , total_points)