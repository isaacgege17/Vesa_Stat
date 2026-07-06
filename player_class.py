class Team:
    def __init__(self, name, wins, losses):
        self.name = name
        self.wins = wins
        self.losses = losses
team1 = Team("Lakers",33,5)
team2 = Team("Mavericks",15,4)
print(team1)
print(team2)