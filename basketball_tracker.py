def title():
    print("BASKETBALL TRACKER")
title()
def goodbye():
    print("Thanks for using basketball tracker!")
no_players = int(input("Enter number of players: "))
players = []
points = []
rebounds = []
assists = []
fouls =[]
for i in range(no_players):
    player_name = input("Player name: ")
    player_points = int(input("Points scored: "))
    player_rebounds = int(input("Rebounds: "))
    player_assists = int(input("Assists: "))
    player_fouls = int(input("Fouls: "))

    players.append(player_name)
    points.append(player_points)
    rebounds.append(player_rebounds)
    assists.append(player_assists)
    fouls.append(player_fouls)
for i in range(len(players)):
    print()
    print("Player Name: ", players[i].upper())
    print("Points : ", points[i])
    print("Rebounds: ", rebounds[i])
    print("Assists: ", assists[i])
    print("Fouls: ", fouls[i])
    print()
    if points[i] >= 30:
        print("MVP Performance! ")
    elif points[i] >= 20:
        print("Great Performance! ")
    else:
        print("Keep working hard! ")

goodbye()



