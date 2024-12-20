from random import *
from utility_functions import*
import json
def treasure_room() :
    with open("Data\TRClues.json", "r", encoding="utf-8") as f:
        tv_game = json.load(f)
        year = str(randint(2015,2019))
        D = tv_game["Fort Boyard"][year]
        show = D[choice(list(D.keys()))]
        print("Clues:\n-{}\n-{}\n-{}".format(show["Clues"][0],show["Clues"][1],show["Clues"][2]))
        correct_answer = show["CODE-WORD"]
        tries = 3
        while tries>0 :
            answer = input("code word : ")
            answer2 = ""
            for i in answer:
                if 122 >= ord(i) >= 97:
                    answer2 += chr(ord(i) - 32)
                else:
                    answer2 += i
            if answer2 == correct_answer :
                print("You're right, you won")
                return True
            elif tries > 1 :
                tries -= 1
                print("Missed, number of tries left : {}, here is another hint : {}".format(tries, show["Clues"][-(tries+1)]))
            else : tries -= 1
        print("What a pity, the last hint was : {} and the answer was {}".format(show["Clues"][5],correct_answer))

treasure_room()