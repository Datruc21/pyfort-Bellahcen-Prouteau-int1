from random import *
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
            if answer == correct_answer :
                print("You're right, you won")
                return True
            else :
                tries -= 1
                print("Missed, number of tries left : {}, here is another hint : {}".format(tries, show["Clues"][-(tries+1)]))
        print("What a pity, the last hint was : {} and the answer was {}".format(show["Clues"][5],correct_answer))

treasure_room()