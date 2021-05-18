cmd = ""
started = False

while True:
    cmd = input("> ").lower()
    if cmd == "start":
        if started:
            print("The car already started")
        else:
            started = True
            print("The car started ....")
    elif cmd == "stop":
        if not started:
            print("The car already stopped!!!")
        else:
            started = False
            print("The car stopped ....")
    elif cmd == "help":
        print("start - start the car")
        print("stop - stop the car")
        print("quit - to quit")
    elif cmd == "quit":
        break
    else:
        print("Sorry, we dont understand")