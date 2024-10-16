import random

MAX_TRIES = 3

def StartGame():
    currentTries = MAX_TRIES
    randomNumber = random.randint(1,10)
    while(currentTries > 0):

        userSelecction = input("Select a number between 1 - 10:\n    ")
        userSelecction = int(userSelecction)

        if(userSelecction == randomNumber):
            print(f"You Win! :)\nThe winner number is... number {randomNumber}")
        elif(userSelecction > randomNumber):
            print(f"    The number to answer is lower than {userSelecction}")
        else:
            print(f"    The number to answer is greather than {userSelecction}")

        currentTries -= 1
    
    print(f"You Loose :(\nThe winner number is... number {randomNumber}")
