"""         PYFORT by Maël and Jalil
THe Père Fouras' challenge module (done by Jalil and Maël), enables to have access to one of the many riddles and (potentially) solve it """
import json
from random import *

def load_ridles(file) :
    """Load the file and put its content into a usable format (a list), then return it"""
    with open(file, "r", encoding="utf-8") as f:
        data = json.load(f)
        L = []
        for i in data :
            d = {}
            for key in i.keys() :
                if key == "question" or key == "answer" :
                    d[key] = i[key]
            L.append(d)
    return L

def pere_fouras_riddles():
    """Select a random riddle from the list previously created and show it to the player
    The player can answer in with uppercase or lowercase letters (or both) and with or without "The "
     Return True if the game is won, False otherwise"""
    tries = 3
    riddles = load_ridles("Data/PFRiddles.json")
    challenge = choice(riddles)
    print(challenge["question"])
    while tries>0 :
        answer1 = input("Answer : ")
        answer2 = ""
        for i in answer1 :
            if 90>=ord(i)>=65 :
                answer2 += chr(ord(i)+32)
            else :
                answer2 += i
        question = ""
        for i in range(4,len(challenge["answer"])) :
            if 90>=ord(challenge["answer"][i])>=65 :
                question += chr(ord(challenge["answer"][i])+32)
            else :
                question += challenge["answer"][i]
        if "the " not in answer2 and answer2 == question :  #answer et answer
            print("Correct, you win a key !")
            return True
        elif "the " in answer2 and question in answer2 and abs(len(answer2)-4-len(question)) == 0 :
            print("Correct, you win a key !")
            return True
        else :
            print("Wrong, try again")
        tries -= 1
    print("Tough luck, the answer was {}".format(challenge["answer"]))
    return False










