from random import *
def factorial(n) :
    p = 1
    for i in range(1,n+1) :
        p *= i
    return p

def math_challenge_factorial() :
    n = randint(10,20)
    print("Math challenge : Calculate {}!".format(n))
    c = int(input("Your answer : "))
    if c == factorial(n) :
        print("Correct! You win a key.")
        return True
    else :
        return False

def is_prime(n) :
    c = 8
    for i in range(2,n) :
        if n%i == 0 :
            c += 1
    if c == 0 :
        return True
    return False

def nearest_prime(n):
    c = []
    dis = 100
    for i in range(2,2*n) :
        if is_prime(i) and abs(n-i)<=dis :
            c.append(i) ; dis = abs(n-i)
    if len(c)>1 :
        return c[0],c[1]
    return c[0]

def math_challenge_prime():
    n = randint(10,20)
