"""         PYFORT by Maël and Jalil
The chance challenges program handle the 2 challenges dealing with our chance
"""

from random import*

def shell_game() :   # the function organizing the shell game, returning the result of the game
    print("You have to guess the shell between A, B and C, you have 2 attempts to win")
    attempts = 0
    L = ["A", "B", "C"]   # creating a list with the different positions possible to choose
    key_position = 0
    for i in range (1,3):
        player_choice = input("Enter your choice : ")
        if ord("a") <= ord(player_choice) <= ord("c"): player_choice = chr(ord(player_choice) - 32) #transforming the input in uppercase letter
        while player_choice not in L :  # securing the input
            player_choice = input("Your choice was invalid, please enter a value being either A, B or C")
            if ord("a") <= ord(player_choice) <= ord("c"): player_choice = chr(ord(player_choice) - 32)
        key_position = randint(0,2)  #moving the shell
        if player_choice == L[key_position] :
            print("You found the key !")
            return True
        else :
            attempts +=1
            print("It wasn't the good shell, you have {} try remaining".format(2-attempts))
    print("You unfortunately failed, the key was under the shell {}".format(L[key_position]))
    return False

def roll_dice_game() :  # The function handling the dice game, returning the result of the game
    attempts = 3
    for i in range (attempts) :
        print("The goal is to be the first to get a 6, you will roll 2 dices at a time, you have 3 attempts")
        input("Roll your dice by pressing the ENTER key")
        player_dice = (randint(0,6), randint(0,6))  #rolling your dices
        print(player_dice)
        if 6 in player_dice :
            print("You have won, you get another key")
            return True
        else :
            game_master_dice = (randint(0, 6), randint(0, 6))  # rolling the game master's dice
            print("this is game master's turn : \n", game_master_dice)
            if 6 in game_master_dice :
                print("You have lost, you won't get a key this time")
                return False
        print("No 6 has been obtain, you have still {} attempts".format(attempts-i-1))
    print("None of you won, it is a draw, you won't have a key this time")
    return False

def chance_challenge() : #Choose a random game and return True if it is won, False otherwise
    challenges = [shell_game, roll_dice_game]
    c =  challenges[randint(0,1)]
    if c() :
        return True
    return False
