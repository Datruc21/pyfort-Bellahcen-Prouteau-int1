from random import *
from utility_functions import *

def factorial(n) : #The function that return the factorial of a number n
    p = 1
    for i in range(1,n+1) :
        p *= i
    return p

def math_challenge_factorial() : #The first challenge
    n = randint(1,10)
    print("Math challenge : Calculate {}!".format(n))
    c = int(input("Your answer : "))
    if c == factorial(n) :
        print("Correct! You win a key.")
        AddKey()
        return True
    print("A pity, the answer was {}".format(factorial(n)))
    return False

def is_prime(n) : #Check whether a number n is prime or not
    c = 0
    for i in range(2,n) :
        if n%i == 0 :
            c += 1
    if c == 0 :
        return True
    return False

def nearest_prime(n): #a function that return the nearest prime number to a number n
    c = 0
    dis = 100
    for i in range(2,2*n) :
        if is_prime(i) and abs(n-i)<=dis :
            c = i
            dis = abs(n-i)
    if c != n+dis and is_prime(n+dis):
        return [c, n+dis]
    elif c != n-dis and is_prime(n-dis) :
        return [c, n-dis]
    return [c,"none"]

def math_challenge_prime(): #The second challenge
    n = randint(10,20)
    print("Find the closest prime number to {}".format(n))
    c = int(input("Your answer : "))
    if c in nearest_prime(n) :
        print("Congrats! You deserve a key !")
        return True
    print("What a pity, it's wrong!")
    return False

def math_roulette_challenge(): # The third math challenge
    L = [randint(1,20) for i in range(5)]
    op = ["+","-","*"]
    c = choice(op)
    print("Numbers of the roulette : {}".format(L))
    if c == "+" :
        print("Calculate the sum of all the numbers")
        k = int(input("Your answer : "))
        answer = 0
        for i in L :
            answer += i
    elif c == "*" :
        print("Calculate the product of all the numbers")
        k = int(input("Your answer : "))
        answer = 1
        for i in L:
            answer *= i
    else :
        print("Calculate the difference of all numbers from left to right : ")
        k = int(input("Your answer : "))
        answer = L[0]
        for i in range(1,len(L)) :
            answer -= L[i]
    if k == answer :
        print("That's a good answer, you win a key!")
        return True
    print("What a shame, you lost!")
    return False

challenges = [math_challenge_factorial, math_challenge_prime, math_roulette_challenge()]

def math_challenge() :
    return challenges[randint(0,2)]
