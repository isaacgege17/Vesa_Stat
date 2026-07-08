def title():
    print("BASKETBALL TRACKER")
title()
def goodbye():
    print("Thanks for using basketball tracker!")
team_name = input("Team name: ")
coach_name = input("Coach name: ")
venue_name = input("Venue name: ")
no_players = int(input("Number of players: "))
game_info = {
    "Team Name" : team_name,
    "Coach Name" : coach_name,
    "Venue Name" : venue_name,
    "Number of Players" : no_players
}
def info():
    print("/nTeam Name: ", game_info["Team Name"].upper())
    print("Coach Name: ", game_info["Coach Name"].upper())
    print("Venue Name: ", game_info["Venue Name"].upper())
    print("Number of Players: ", game_info["Number of Players"])
    print("________________________")
    print()
players = []
class Player:
    def __init__(self, name, points, rebounds, assists, fouls):
        self.name = name
        self.points = points
        self.rebounds = rebounds
        self.assists = assists
        self.fouls = fouls
for i in range(no_players):
    name = input("Player name: ")
    points = int(input("Points scored: "))
    rebounds = int(input("Rebounds: "))
    assists = int(input("Assists: "))
    fouls = int(input("Fouls: "))
    player = Player(name, points, rebounds, assists, fouls)
    players.append(player)
def player_performance(player_points):
    if player_points >= 30:
        return "MVP Performance! "
    elif player_points >= 20:
        return "Great Performance! "
    else:
        return "Keep working hard! "
    print("______________________")
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
        file.write(player.name + "\n")
        file.write(str(player.points) + "\n")
        file.write(str(player.rebounds) + "\n")
        file.write(str(player.assists) + "\n")
        file.write(str(player.fouls) + "\n")
        print("Roster saved")
    else:
        print("Roster not saved")
file.close()
goodbye()



