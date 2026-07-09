from functions import title, player_performance, goodbye
title()
from player import Player
team_name = input("Team name: ")
coach_name = input("Coach name: ")
venue_name = input("Venue name: ")
no_players = int(input("Number of players: "))
game_info = {
    "Team Name" : team_name.upper(),
    "Coach Name" : coach_name.upper(),
    "Venue Name" : venue_name.upper(),
    "Number of Players" : no_players
}
def info():
    print("\n" , "Team Name: ", game_info["Team Name"])
    print("Coach Name: ", game_info["Coach Name"])
    print("Venue Name: ", game_info["Venue Name"])
    print("Number of Players: ", game_info["Number of Players"])
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
    print("Player Name: ", player.name.upper())
    print("Points : ", player.points)
    print("Rebounds: ", player.rebounds)
    print("Assists: ", player.assists)
    print("Fouls: ", player.fouls)
    print()
    print(player_performance(player.points))
choice = input("Would you like to save this roster? (yes/no): ")
file = open("roster.txt", "w")
for player in players:
    if choice.lower() == "yes":
        file.write(f"{player.name}\n")
        file.write(f"{player.points}\n")
        file.write(f"{player.rebounds}\n")
        file.write(f"{player.assists}\n")
        file.write(f"{player.fouls}\n")
        print("Roster saved")
    else:
        print("Roster not saved")
file.close()
goodbye()



