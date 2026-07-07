def player_grade(points):
    if points >= 30:
        return "A"
    elif points >= 20:
        return "B"
    elif points >= 10:
        return "C"
    else:
        return "D"
grade = int(input("Points: "))
print(player_grade(grade))