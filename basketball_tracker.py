print("BASKETBALL TRACKER")
player_name = input("Enter player name: ")
points_scored = int(input("Enter points scored: "))
rebounds = int(input("Enter rebounds: "))
assists = int(input("Enter assists: "))
total = points_scored + rebounds + assists
print("Player Name: ", player_name.upper())
print("Points Scored: ", points_scored)
print("Rebounds: ", rebounds)
print("Assists: ", assists)
print()
print("Total Stats: ", total)
print()
if points_scored >= 30:
    print("MVP Performance! ")
elif points_scored >= 20:
    print("Great Performance! ")
else:
    print("Keep working hard! ")


