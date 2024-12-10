import json
from random import *

def load_ridles(file) :
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
    tries = 3
    riddles = load_ridles("Data\PFRiddles.json")
    challenge = choice(riddles)
    print(challenge)
    print("Please enter your answer in the following format : the 'answer'")
    print(challenge["question"])
    while tries>0 :
        answer1 = input("Answer : ")
        answer2 = ""
        for i in answer1 :
            if 90>=ord(i)>=65 :
                answer2 += chr(ord(i)+32)
            else :
                answer2 += i



        count = 0
        k = 0
        while k<len(challenge["answer"]) and k<len(answer2) :
            if challenge["answer"][k] == answer2[k] or challenge["answer"][k] == chr(ord(answer2[k])-32): #second condition is for the capital letter at the beginning,
                count += 1                                                                                 #since our whole answer is in lowercase letters
            k += 1


        if count == len(challenge["answer"]):
            print("That's the good answer, you won a key")
            return True
        else :
            print("Wrong, try again")
            tries -= 1
    print("Tough luck, the answer was {}".format(challenge["answer"]))
    return False









