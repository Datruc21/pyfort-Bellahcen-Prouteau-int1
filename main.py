"""         PYFORT by Maël and Jalil
The main file (done by Maël), used to run the game"""

from chance_challenges import *
from final_challenge import *
from math_challenges import *
from logical_challenges import *
from pere_fouras_challenge import *
from utility_functions import *

def game (): # The main function, running the game
    team = introduction()
    while count_key(team) < 3 :  #The loop calling all the challenges
        player = choose_player(team)
        if challenges_menu()() :  #It verifies if you won for the challenge chosen (see utility function)
            team[player]["keys_won"] += 1
            print("You now have : {} keys !\n".format(count_key(team)))
    print("Congrats for your keys, now it's time for the true challenge, the treasure room !\n")
    if treasure_room() : # It calls the final challenge and verifies if you won
        print("You won !!, here is your team !", team)
        record_history(team, True)  # Save the results of the team in a file
    else :
        print("What a noob, not this time, maybe another day")
        record_history(team, False) # Save the results of the team in a file

game()
