i = 1
while i <= 3:
    number = int(input("Guest : "))
    i = i + 1
    if number == 9:
        print("You win!!")
        break
else:
    print("You lost")


