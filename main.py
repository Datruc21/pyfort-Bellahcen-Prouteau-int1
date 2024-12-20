from chance_challenges import *
from final_challenge import *
from math_challenges import *
from logical_challenges import *
from pere_fouras_challenge import *
from utility_functions import *

def game ():
    team = introduction()
    while count_key(team) < 3 :
        player = choose_player(team)
        if challenges_menu()() :
            team[player]["keys_won"] += 1
            print("You now have : {} keys !\n".format(count_key(team)))
    print("Congrats for your keys, now it's time for the true challenge, the treasure room !\n")
    if treasure_room() :
        print("You won !!, here is your team !", team)
    else : print("What a noob, not this time, maybe another day")

game()
