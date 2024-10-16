import random

MAX_SCORE = 3
SELECTIONS = { 
    0 : "Rock",
    1 : "Paper",
    2 : "Scissor"
}

def StartGame():
    userScore = 0
    iaScore = 0
    gameOver = False
    while(gameOver == False):
        # Ia selection
        iaSelection = random.randint(0,2)

        # User selection
        userSelection = input(f"Select an option:\n    (1) - {SELECTIONS[0]}\n    (2) - {SELECTIONS[1]}\n    (3) - {SELECTIONS[2]}\n")
        userSelection = int(userSelection) - 1

        # Comprobe Game
        print(f"(you) {SELECTIONS[userSelection]} Vs (bot) {SELECTIONS[iaSelection]}")
        result = ComprobeGame(userSelection, iaSelection)

        # Print game result
        if(result == 1):
            print("Its a DRAW!")
        elif (result == 2):
            print("You WINNED!")
            userScore += 1
        else:
            print("You LOOSED!")
            iaScore += 1

        # Print player scores
        print(f"Your Score: {userScore}\nBot Score: {iaScore}")

        gameOver = ComprobeGameOver(userScore, iaScore)

        
    # While END

def ComprobeGame(user, ia):
    WINNING_RULES = {
    0: 2,
    1: 0,
    2: 1
    }
    
    if(user == ia):
        return 1    # Draw
    elif (WINNING_RULES[user] == ia):
        return 2    # Comprobe if user win
    
    return 0        # Ia Win

def ComprobeGameOver(user, ia):
    # Gameover Handler
    result = False
    if(user >= MAX_SCORE or ia >= MAX_SCORE):
        result = True

        if(user >= MAX_SCORE):
            print("YOU Winned the Match!")
        else:
            print("YOU Loosed the Match :(")
    
    return result