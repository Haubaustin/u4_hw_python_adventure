# Create your own adventure with python here
def restart():
    print("Would you like to play? 'Y'/'N'")
    restart = input()
    if restart == "Y" or 'y':
        gamestart()
  


def gamestart():
    print("What is your name?")
    name = input()

    print("Hello " + name + "!")
    print("You are an NFL offensive Coordinator trying to score a touchdown on the last play of the game. Would you like to run the ball or pass the ball? Enter 'R' for run or 'P' for pass")
    passrun = input()

    if passrun == "R" or "r":
        print("Would you like to run the ball inside or outside? Inside 'I' or Outside 'O'")
        insideout = input()
        if insideout == "I" or "i":
            print("You chose to run the ball inside! Great Choice! Who is going to carry the ball into the endzone? Your 'QB', 'RB', or 'FB'")
            ballcarrier = input()
            if ballcarrier == "QB" or "qb" or "Qb" or "qB":
                print("Lucky for you your QB is Tom Brady. Like he always does, which is win, he executed a QB sneak to perfection and drove the ball into the endzone.")
                restart()
            elif ballcarrier == "RB" or "Rb" or "rb" or "rB":
                print("Oh no! Your right guard missed his assignment and the defensive tackle came in unblocked. Your running back just got hit so hard hes bascially asleep on the field")
                restart()
            elif ballcarrier == "FB" or "fb" or "Fb" or "fB":
                print("Best Choice. You're probably an AWL from Pardon My Take. Your Fullback easily trucks over the Middle Linebacker into the Endzone")
                restart()
        elif insideout == "O" or "o":
            print("You chose to run the ball outside! Great Choice! Who is going to carry the ball into the endzone? Your 'QB', 'RB', or 'FB'")
            ballcarrier2 = input()
            if ballcarrier2 == "QB" or "qb" or "Qb" or "qB":
                print("Unlucky for you your QB is Tom Brady. He may be the GOAT but he's definetly not the GOAT of running the ball. There's not a weird enough diet in the world to make Tom Brady fast enough to outrun a defender.")
                restart()
            elif ballcarrier2 == "RB" or "Rb" or "rb" or "rB":
                print("Oh no! Your right guard missed his assignment and the defensive tackle came in unblocked. Your running back just got hit so hard hes bascially asleep on the field")
                restart()
            elif ballcarrier2 == "FB" or "fb" or "Fb" or "fB":
                print("Bold strategy Cotton lets see how this plays out for you. Your fullback decided that was a bad idea and takes the ball up the middle instead bailing you out. Thats a touchdown ")
                restart()
    elif passrun == "P" or "p":
        print("Where would you like to throw the ball? Flats or Back of the endzone. Please enter 'F' or 'B'")
        passloc = input()
        if passloc == "F" or "f":
            print("You chose the flats. Who would you like to pass it to? Your Runningback or Wide Reciever? Please Enter 'W' or 'R'")
            reciever = input()
            if reciever == "W" or "w":
                print("Your Wide Reciever drops to the floor to catch a low bullet and just pulls it in within the endzone. Touchdown!")
                restart()
            elif reciever == "R" or "r":
                print("Fumbled Snap. Your QB barely has enough time to grab the ball before hes sacked.")
                restart()
        elif passloc == "B" or "b":
            print("Your Wide Reciever High points the ball and you score a touchdown")
            restart()

gamestart()

    


