cmd = ""
while True:
    cmd = input("> ").lower()
    if cmd == "start":
        print("The car started ....")
    elif cmd == "stop":
        print("The car stopped ....")
    elif cmd == "help":
        print("start - start the car")
        print("stop - stop the car")
        print("quit - to quit")
    elif cmd == "quit":
        break
    else:
        print("Sorry, we dont understand")