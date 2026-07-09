def title():
    print("BASKETBALL TRACKER")
def goodbye():
    print("Thanks for using basketball tracker!")
def player_performance(player_points):
    if player_points >= 30:
        return "MVP Performance! "
    elif player_points >= 20:
        return "Great Performance! "
    else:
        return "Keep working hard! "