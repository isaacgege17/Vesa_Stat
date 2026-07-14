from player import Player
players = []
def register_player():
    p_name = input("Player name: ")
    p_points = int(input("Points scored: "))
    p_rebounds = int(input("Rebounds: "))
    p_assists = int(input("Assists: "))
    p_fouls = int(input("Fouls: "))
    player = Player(p_name, p_points, p_rebounds, p_assists, p_fouls)
    players.append(player)
def view_roster():
    file = open("rosters.txt", "r")
    lines = file.readlines()
    for line in lines:
        print(line)
    file.close()
def save_roster():
    file = open("rosters.txt", "w")
    for player in players:
        file.write(f"Player Name: {player.name}\n")
        file.write(f"Points: {player.points}\n")
        file.write(f"Rebounds: {player.rebounds}\n")
        file.write(f"Assists: {player.assists}\n")
        file.write(f"Fouls: {player.fouls}\n")
    file.close()
    print("Roster saved")
try:
    while True:
        print(f"\n1. Register\n2. View roster\n3. Save roster\n4. Exit\n")
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            register_player()
        elif choice == "2":
            view_roster()
        elif choice == "3":
            save_roster()
        elif choice == "4":
            print("Goodbye")
            break
        else:
            print("Invalid choice")
except ValueError:
    print("Invalid choice")


