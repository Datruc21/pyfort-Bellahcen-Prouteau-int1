"""         PYFORT by Maël and Jalil
THe maths challenge module (done by Jalil), used to give maths challenge to the contenders"""
from random import *
from utility_functions import *

def factorial(n) :
    """This function takes an integer as a parameter and return its factorial"""
    p = 1
    for i in range(1,n+1) :
        p *= i
    return p

def math_challenge_factorial() :
    """Chooses a random number between 1 and 10, and ask the user for its factorial, if answer is
    correct, return True, else False"""
    n = randint(1,10)
    print("Math challenge : Calculate {}!".format(n))
    c = int(input("Your answer : "))
    while c<0 :
        c = int(input("Please enter a positive integer : "))
    if c == factorial(n) :
        print("Correct! You win a key.")
        return True
    print("A pity, the answer was {}".format(factorial(n)))
    return False

def is_prime(n) : #Check whether a number n is prime or not
    """Test the integer parameter, return True is it's a prime, else False"""
    c = 0
    for i in range(2,n) :
        if n%i == 0 :
            c += 1
    if c == 0 :
        return True
    return False

def nearest_prime(n): #a function that return the nearest prime number to a number n
    """Return the nearest prime number of the parameter. Possible outcomes if n = 1, return [2,"none"] if n = 5, return [3,7]
    (they are at the same distance, so both are the nearest prime)"""
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

def math_challenge_prime():
    """Chooses a random number between 10 and 20 and ask the nearest prime number (if there's two answers, both will
    be considered correct) return True if the answer is correct, else False"""
    n = randint(10,20)
    print("Find the closest prime number to {}".format(n))
    c = int(input("Your answer : "))
    while c<0 :
        c = int(input("Please enter a positive integer : "))
    if c in nearest_prime(n) :
        print("Congrats! You deserve a key !")
        return True
    print("What a pity, it's wrong!")
    return False

def math_roulette_challenge():
    """Chooses one symbol randomly and a list of 5 random integers between 1 and 20
     Ask the user to compute the operation associated with the selected symbol
    If it's a subtraction with [a,b,c,d,e] the expected result will be a-b-c-d-e
    return True for a correct answer, False otherwise"""
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


def math_challenge() :
    """Select a challenge randomly from this module and return True if the player is correct, False otherwise"""
    challenges = [math_challenge_factorial, math_challenge_prime, math_roulette_challenge]
    c = challenges[randint(0,2)]
    if c() :
        return True
    return False

