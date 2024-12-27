"""         PYFORT by Maël and Jalil
The final challenge program handling the last trial (done by Maël)
"""

from random import *
from utility_functions import*
import json
def treasure_room() : #The main function simulating the trial, it will return the result, and True if the player wins, False otherwise
    with open("Data/TRClues.json", "r", encoding="utf-8") as f:
        tv_game = json.load(f)
        year = str(randint(2015,2019))
        season = tv_game["Fort Boyard"][year]
        show = season[choice(list(season.keys()))]
        remaining_clues = show["Clues"]   #saving the clues which were not displayed yet to choose a random one each time next line
        print("Clues:\n-{}\n-{}\n-{}".format(remaining_clues.pop(randint(0,len(remaining_clues)-1)),remaining_clues.pop(randint(0,len(remaining_clues)-1)),remaining_clues.pop(randint(0,len(remaining_clues)-1))))
        correct_answer = show["CODE-WORD"]
        tries = 3
        while tries>0 :
            answer = input("code word : ")
            answer2 = ""
            for i in answer:   #setting all the letters in uppercase to check for the answer
                if 122 >= ord(i) >= 97:
                    answer2 += chr(ord(i) - 32)
                else:
                    answer2 += i
            if answer2 == correct_answer :
                print("You're right, you won")
                return True
            elif tries > 1 :
                tries -= 1
                print("Missed, number of tries left : {}, here is another hint : {}".format(tries, remaining_clues.pop(randint(0,len(remaining_clues)-1))))  # display a new hint and tell them the number of tries left
            else : tries -= 1
        print("What a pity, the answer was {}".format(correct_answer))
        return False
