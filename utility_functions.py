from random import *

key = 0

def introduction() :
    print("Your goal is to get 3 keys to access the treasure room, in order to get them, you will have to complete challenges")

def AddKey() :
    global  key
    key += 1

def compose_team():
    player_number = int(input("Enter the number of player in your team : \n"))
    while 3<player_number<0 :
        player_number = int(input("You cannot have more than 3 players in your team : \n"))
    player = [{}, {}, {}]
    for i in range(player_number) :
        player[i]["name"] = input("Enter the name of this player :\n")
        player[i]["profession"] = input("Enter its profession :\n")
        player[i]["leader"] = input("Is it the leader ? Enter yes if this person is.\n") == 'yes'
        player[i]["keys_won"] = 0

    leader_number = 0
    for i in range(player_number) : # We check whether there is one leader or not, we will keep the first one if there are many or designate the first player if there is noone.

        if player[i]["leader"]: leader_number+=1
    if leader_number == 0 :
        player[0]['leader'] = True

    return player

def challenges_menu():
    challenges_available = ["Mathematics challenge", "Logic challenge", "Chance challenge", "Pere Fouras's riddle"]
    return challenges_available[int(input(" 1.Mathematics challenge \n 2. Logic challenge \n 3. Chance challenge \n 4. Père Fouras's riddle\n")) - 1]

def choose_player(team) :
    for i in range (len(team)) :
        if team[i]["leader"] == True :
            leader = "Leader"
        else:
            leader = "Member"
        print("{}. {} ({}) {}".format(i+1, team[i]['name'], team[i]["profession"], leader))