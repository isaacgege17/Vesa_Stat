no_players = int(input("Number of players: "))
class Player:
    def __init__(self, name, points):
        self.name = name
        self.points = points
file = open("players.txt" , "w")
for i in range(no_players):
    p_name = input("Player name: ")
    p_points = input("Player points: ")
    players_info = Player(p_name,p_points)

    file.write(players_info.name + "\n")
    file.write(str(players_info.points) + "\n")
file.close()

file = open("players.txt" , "r")
print(file.read())
file.close()
