from random import*

def shell_game() :
    print("You have to guess the shell between A, B and C, you have 2 attempts to win")
    attempts = 0
    L = ["A", "B", "C"]
    for i in range (1,3):
        choice = input("Enter your choice : ")
        if ord("a") <= ord(choice) <= ord("c"): choice = chr(ord(choice) - 32)
        while choice not in L :
            choice = input("Your choice was invalid, please enter a value being either A, B or C")
            if ord("a") <= ord(choice) <= ord("c"): choice = chr(ord(choice) - 32)
        key_position = randint(0,2)
        if choice == L[key_position] :
            print("You found the key !")
            return True
        else :
            attempts +=1
            print("It wasn't the good shell, you have {} try remaining".format(2-attempts))
    print("You unfortunately failed, the key was under the shell {}".format(L[key_position]))
    return False

def roll_dice_game() :
    attempts = 3
    player_dice = ()
    game_master_dice = ()
    for i in range (attempts) :
        player_dice = ()
        game_master_dice = ()
        print("The goal is to be the first to get a 6, you will roll 2 dices at a time, you have 3 attempts")
        (input("Roll your dice by pressing the ENTER key"))
        player_dice = (randint(0,6), randint(0,6))
        print(player_dice)
        if 6 in player_dice :
            print("You have won, you get another key")
            return True
        else :
            game_master_dice = (randint(0, 6), randint(0, 6))
            print(game_master_dice)
            if 6 in game_master_dice :
                print("You have lost, you won't get a key this time")
                return False
        print("No 6 has been obtain, you have still {} attempts".format(attempts-i-1))
    print("None of you won, it is a draw, you won't have a key this time")
    return False

def chance_challenge() :
    challenges = [shell_game, roll_dice_game]
    c =  challenges[randint(0,1)]
    if c() :
        return True
    return False
