"""         PYFORT by Maël and Jalil
The utility functions program (done by Maël) handle every function being called in the main program
"""

from random import *
from math_challenges import *
from logical_challenges import *
from chance_challenges import *
from pere_fouras_challenge import *

def introduction() :  # the function describing their goal for the player at the beginning, returns the team
    print("Your goal is to get 3 keys to access the treasure room, in order to get them, you will have to complete challenges")
    return compose_team()  # call the function to create the team

def compose_team(): #create the team and return it (team)
    player_number = int(input("Enter the number of player in your team (maximum 3): \n"))
    while 3<player_number<0 :
        player_number = int(input("You cannot have more than 3 players in your team : \n"))
    team = []
    for i in range(player_number) :  # for every player, stores the information in a dictionary
        team.append({})
        team[i]["name"] = input("Enter the name of this player :\n")
        team[i]["profession"] = input("Enter its profession :\n")
        team[i]["leader"] = input("Is it the leader ? Enter yes if this person is.\n") == 'yes'
        team[i]["keys_won"] = 0
    leader_number = 0
    for i in range (len(team)) :  # check whether the team has a leader
        if team[i]["leader"]:
            leader_number = 1
            break
    if leader_number == 0 :
        team[0]["leader"] = True  # If noone is the leader, by default set the first player as one
    return team

def challenges_menu():  #A function displaying the different types of challenges available and returning the choice as an integer
    challenges_available = [math_challenge, battleship_game, chance_challenge, pere_fouras_riddles]
    return challenges_available[int(input(" 1.Mathematics challenge \n 2.Logical challenge \n 3.Chance challenge \n 4.Père Fouras' riddle\n")) - 1]

def choose_player(team) : # A function asking to choose one player in the team to participate in the next challenge, returning the player place in the team
    for i in range (len(team)) : # the loop is setting the leader state in their dico
        if team[i]["leader"]:
            leader = "Leader"
        else:
            leader = "Member"
        print("{}. {} ({}) {}".format(i+1, team[i]['name'], team[i]["profession"], leader))
    return int(input("Enter the number of the player competing for the next trial : \n"))-1

def count_key(team) :
    keys = 0
    for i in range(len(team)) : keys += team[i]["keys_won"]
    return keys

def record_history(team) : # It adds in a file the history of the tries
    with open ("history.txt", "a") as f1 :
        f1.write(str(team) + "\n")