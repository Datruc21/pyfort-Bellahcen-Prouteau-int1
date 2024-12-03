from random import *


def Reset() :
    global  key
    key = 0

def AddKey() :
    global  key
    key += 1

def ChoosePlayer(p1, p2 = "", p3 = "") :

    list_player = [p1]
    if p2 != "" :
        list_player.append(p2)
        if p3!= "" : list_player.append(p3)

    player = randint(0,len(list_player)-1)
    return list_player[player]
