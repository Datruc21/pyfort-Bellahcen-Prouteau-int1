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
        player[i][1] = input("Enter the name of this player :")
        player[i][2] = input("Enter its profession :")
        player[i][3] = input("Is it the leader ? Enter yes if this person is.") == 'yes'

    print(player)


def ChoosePlayer(p1, p2 = "", p3 = "") :

    list_player = [p1]
    if p2 != "" :
        list_player.append(p2)
        if p3!= "" : list_player.append(p3)

    player = randint(0,len(list_player)-1)
    return list_player[player]
