from random import *
from utility_functions import *

def factorial(n) :
    p = 1
    for i in range(1,n+1) :
        p *= i
    return p

def math_challenge_factorial() :
    n = randint(1,10)
    print("Math challenge : Calculate {}!".format(n))
    c = int(input("Your answer : "))
    if c == factorial(n) :
        print("Correct! You win a key.")
        AddKey()
        return True
    else :
        return False

def is_prime(n) :
    c = 0
    for i in range(2,n) :
        if n%i == 0 :
            c += 1
    if c == 0 :
        return True
    return False

def nearest_prime(n):
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
    n = randint(10,20)
    print("Find the closest prime number to {}".format(n))
    c = int(input("Your answer : "))
    if c in nearest_prime(n) :
        print("Congrats! You deserve a key !")
        return True
    print("What a pity, it's wrong!")
    return False
