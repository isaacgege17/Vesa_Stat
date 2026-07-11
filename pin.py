correct_pin = 1234
while True:
    pin = int(input("Enter four digit pin: "))
    if pin == correct_pin:
        print("Access Granted!")
        break
    else:
        print("Incorrect Pin!")