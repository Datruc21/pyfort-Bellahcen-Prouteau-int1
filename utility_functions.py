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
    team_name = input("Enter your team name :\n")
    player_number = int(input("Enter the number of player in your team (maximum 3): \n"))
    while player_number<=0 or 3<player_number:
        player_number = int(input("You cannot have more than 3 (or less than 1) players in your team : \n"))
    team = [team_name]
    for i in range(player_number) :  # for every player, stores the information in a dictionary
        team.append({})
        team[i+1]["name"] = input("Enter the name of this player :\n")
        team[i+1]["profession"] = input("Enter their profession :\n")
        team[i+1]["leader"] = input("Are they the leader ? Enter yes if this person is.\n") == 'yes'
        team[i+1]["keys_won"] = 0
    leader_number = 0
    for i in range (1,len(team)) :  # check whether the team has a leader
        if team[i]["leader"]:
            leader_number = 1
            break
    if leader_number == 0 :
        team[1]["leader"] = True  # If noone is the leader, by default set the first player as one
    return team

def challenges_menu():  #A function displaying the different types of challenges available and returning the choice as an integer
    challenges_available = [math_challenge, battleship_game, chance_challenge, pere_fouras_riddles]
    return challenges_available[int(input(" 1.Mathematics challenge \n 2.Logical challenge \n 3.Chance challenge \n 4.Père Fouras' riddle\n")) - 1]

def choose_player(team) : # A function asking to choose one player in the team to participate in the next challenge, returning the player place in the team
    for i in range (1,len(team)) : # the loop is setting the leader state in their dico
        if team[i]["leader"]:
            leader = "Leader"
        else:
            leader = "Member"
        print("{}. {} ({}) {}".format(i, team[i]['name'], team[i]["profession"], leader))
    chosen = (int(input("Enter the number of the player competing for the next trial : \n")))
    while chosen not in range(1,len(team)) :
        chosen = (int(input("Enter a valid number for the player competing in the next trial : \n")))
    return chosen

def count_key(team) : # A function that return the total number of keys earn in the team
    keys = 0
    for i in range(1,len(team)) : keys += team[i]["keys_won"]
    return keys

def print_chest(keys) : # A function that display a part of the treasure chest
    prints = {1:"\nThe treasure seems to be closer now ...", 2: "\nEven closer now !", 3 : "\nOne last push !"}
    with open("Chest.txt", "r") as f1 :
        chest = f1.readlines()
        for i in range (keys*6) : #Display lines by multiple of 6
            print(chest[i], end="")
        print(prints[keys])

def record_history(team, result) : # It adds in a file the history of the tries
    with open ("history.txt", "a") as f1 :
        f1.write("Team name : " + team[0]+"\n"+"\n")
        for i in range (1, len(team)) : # Store the stats of every player
            f1.write("Player "+ str(i) +": \n")
            f1.write("Name : "+ str(team[i]["name"] +  "\n"))
            f1.write("Profession : " + str(team[i]["profession"] + "\n"))
            f1.write("Role : ")
            if team[i]["leader"]: f1.write("Leader" + "\n")
            else: f1.write("Member" + "\n")
            f1.write("keys : " + str(team[i]["keys_won"]) + "\n")
        if result : f1.write("And it was a victory ! \n \n")
        else : f1.write("unfortunately not this time \n \n")