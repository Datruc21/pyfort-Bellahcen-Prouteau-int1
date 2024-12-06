from random import *

key = 0

def introduction() :
    print("Your goal is to get 3 keys to access the treasure room, in order to get them, you will have to complete challenges")

def AddKey() :
    global  key
    key += 1

def compose_team():
    player_number = int(input("Enter the number of player in your team : "))
    while 3<player_number<0 :
        player_number = int(input("You cannot have more than 3 players in your team : "))
    player = [{}, {}, {}]
    for i in range(player_number) :
        player[i]["name"] = input("Enter the name of this player :")
        player[i]["profession"] = input("Enter its profession :")
        player[i]["leader"] = input("Is it the leader ? Enter yes if this person is.") == 'yes'
        player[i]["keys_won"] = 0

    for i in range(player_number) : # We check whether there is one leader or not, we will keep the first one if there are many or designate the first player if there is noone.

    print(player)

