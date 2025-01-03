"""         PYFORT by Maël and Jalil
The main file (done by Maël), is used to run the game"""

from chance_challenges import *
from final_challenge import *
from utility_functions import *
from pere_fouras_challenge import *
from logical_challenges import *
from math_challenges import *

def game (): # The main function, running the game
    team = introduction()
    while count_key(team) < 3 :  #The loop calling all the challenges
        player = choose_player(team)
        if challenges_menu()() :  #It verifies if you won for the challenge chosen (see utility function)
            team[player]["keys_won"] += 1
            print("You now have : {} keys !\n".format(count_key(team)))
            print_chest(count_key(team)) # Calls a function to display a part of the chest
    print("Congrats for getting your keys, now it's time for the true challenge, the treasure room !\n")
    print("Now, try to guess the password :")
    if treasure_room() : # It calls the final challenge and verifies if you won
        print("You won !!, here is your team !")
        for i in range(1, len(team)):  # the loop is setting the leader state in their dico and displaying the team
            if team[i]["leader"]:
                leader = "Leader"
            else:
                leader = "Member"
            print("{}. {} ({}) {}".format(i, team[i]['name'], team[i]["profession"], leader))
        print("""
                ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                ⣿⣿⣿⣿⣿⣿⣿⣟⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                ⣿⣿⣿⣿⣿⣿⣿⣿⠀⠈⠙⢿⣿⣿⣿⣿⠟⢁⣠⣀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                ⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠈⠻⣿⣧⡾⠟⠉⠙⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿
                ⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⣀⣤⡶⠟⠋⠁⠀⠀⠀⠀⣀⣄⡉⠛⠿⣿⣿⣿⣿⣿
                ⣿⣿⣿⣿⣿⣿⣿⣿⡿⠞⠋⠁⠀⠀⠀⠀⣀⣤⣶⠿⠛⢉⣠⡴⠾⠛⣿⣤⣿⣿
                ⣿⣛⠋⢩⣷⠟⠋⢁⣤⣄⡀⠀⣀⣤⣶⠿⠛⠉⣠⣴⠾⠛⠁⠀⠀⠀⠸⣿⣿⣿
                ⣿⣿⣿⣾⠛⠷⣦⣄⡈⠙⠿⡿⠟⠋⣀⣤⡶⠟⠋⠀⠀⠀⠀⠀⠀⢀⣤⣿⣿⣿
                ⣿⣿⣿⠇⠀⠀⠀⠉⠛⠷⣦⣤⡶⠟⠋⠁⠀⠀⠀⠀⠀⢀⣠⣴⣾⣿⣿⣿⣿⣿
                ⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⢸⡏⠀⠀⠀⠀⠀⢀⣠⣴⠾⠛⠉⠀⠙⢿⣿⣿⣿⣿
                ⣿⣿⣿⣿⣷⣦⣄⡀⠀⠀⢸⡇⠀⢀⣠⣴⠾⠛⠉⣤⣤⣀⣀⡀⠀⠈⢻⣿⣿⣿
                ⣿⣿⣿⣿⣿⡿⠉⠻⢷⣤⣼⣧⣶⣟⠋⠁⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣶⣿⣿⣿
                ⣿⣿⣿⣿⣿⣧⣶⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿""")
        record_history(team, True)  # Save the results of the team in a file
    else :
        print("What a noob, not this time, maybe another day")
        record_history(team, False) # Save the results of the team in a file

game()
