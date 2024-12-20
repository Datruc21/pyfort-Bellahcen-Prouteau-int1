"""         PYFORT by Maël and Jalil
The utility functions program handle the every function being called in the main program
"""

from random import *


def introduction() :  # the function describing their goal for the player at the beginning
    print("Your goal is to get 3 keys to access the treasure room, in order to get them, you will have to complete challenges")
    compose_team()  # call the function to create the team

def compose_team(): #create the team and return it
    player_number = int(input("Enter the number of player in your team : \n"))
    while 3<player_number<0 :
        player_number = int(input("You cannot have more than 3 players in your team : \n"))
    team = [{}, {}, {}]
    for i in range(player_number) :
        team[i]["name"] = input("Enter the name of this player :\n")
        team[i]["profession"] = input("Enter its profession :\n")
        team[i]["leader"] = input("Is it the leader ? Enter yes if this person is.\n") == 'yes'
        team[i]["keys_won"] = 0
    leader_number = 0
    for i in range (len(team)) :
        print(team)
        if team[i]["leader"]:
            leader_number = 1
            break
    if leader_number == 0 :
        team[1]["leader"] = True
    return team

def challenges_menu():
    challenges_available = ["Mathematics challenge", "Logic challenge", "Chance challenge", "Pere Fouras's riddle"]
    return challenges_available[int(input(" 1.Mathematics challenge \n 2. Logic challenge \n 3. Chance challenge \n 4. Père Fouras's riddle\n")) - 1]

def choose_player(team) :
    for i in range (len(team)) :
        if team[i]["leader"] :
            leader = "Leader"
        else:
            leader = "Member"
        print("{}. {} ({}) {}".format(i+1, team[i]['name'], team[i]["profession"], leader))

def AddKey() :
    global  key
    key += 1