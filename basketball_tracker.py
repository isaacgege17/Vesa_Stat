def title():
    print("BASKETBALL TRACKER")
title()
def goodbye():
    print("Thanks for using basketball tracker!")
players = []
class Player:
    def __init__(self, name, points, rebounds, assists, fouls):
        self.name = name
        self.points = points
        self.rebounds = rebounds
        self.assists = assists
        self.fouls = fouls
no_players = int(input("Number of players: "))
for i in range(no_players):
    name = input("Player name: ")
    points = int(input("Points scored: "))
    rebounds = int(input("Rebounds: "))
    assists = int(input("Assists: "))
    fouls = int(input("Fouls: "))
    player = Player(name, points, rebounds, assists, fouls)
    players.append(player)
print("TEAM ROSTER")
for player in players:
    print()
    print("Player Name: ", player.name.upper())
    print("Points : ", player.points)
    print("Rebounds: ", player.rebounds)
    print("Assists: ", player.assists)
    print("Fouls: ", player.fouls)
    print()
    if player.points >= 30:
        print("MVP Performance! ")
    elif player.points >= 20:
        print("Great Performance! ")
    else:
        print("Keep working hard! ")
    print("______________________")

goodbye()



