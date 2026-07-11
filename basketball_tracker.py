from functions import title, player_performance, goodbye
title()
from player import Player
team_name = input("Team name: ")
coach_name = input("Coach name: ").strip().title()
venue_name = input("Venue name: ").strip().title()
no_players = int(input("Number of players: "))
game_info = {
    "Team Name" : team_name.upper(),
    "Coach Name" : coach_name,
    "Venue Name" : venue_name,
    "Number of Players" : no_players
}
def info():
    print(f"\n Team Name:  {game_info['Team Name']}")
    print(f"Coach Name: {game_info['Coach Name']}")
    print(f"Venue Name: {game_info['Venue Name']}")
    print(f"Number of Players: {game_info['Number of Players']}")
    print("________________________")
    print()
players = []
for i in range(no_players):
    p_name = input("Player name: ")
    p_points = int(input("Points scored: "))
    p_rebounds = int(input("Rebounds: "))
    p_assists = int(input("Assists: "))
    p_fouls = int(input("Fouls: "))
    player = Player(p_name, p_points, p_rebounds, p_assists, p_fouls)
    players.append(player)
info()
print("TEAM ROSTER")
for player in players:
    print()
    print("Player Name: ", player.name.title())
    print("Points : ", player.points)
    print("Rebounds: ", player.rebounds)
    print("Assists: ", player.assists)
    print("Fouls: ", player.fouls)
    print()
    print(player_performance(player.points))
while True:
    choice = input("Would you like to save this roster? (yes/no): ").strip().lower()
    if choice == "yes" or choice == "no":
        break
    print("Please enter yes or no")
if choice == "yes":
    file = open("roster.text", "w")
    for player in players:
        file.write(f"{player.name}\n")
        file.write(f"{player.points}\n")
        file.write(f"{player.rebounds}\n")
        file.write(f"{player.assists}\n")
        file.write(f"{player.fouls}\n")
    file.close()
    print("Roster saved")
else:
    print("Roster not saved")
goodbye()



