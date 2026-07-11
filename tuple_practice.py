team = set()
class Team:
    def __init__(self, name):
        self.name = name
for i in range(5):
    team_name = input(f"Team {i+1}: ").strip().title()
    team1 = Team(team_name)
    team.add(team1)
for team1 in team:
    print(team)