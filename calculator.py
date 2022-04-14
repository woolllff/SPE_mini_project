from math import factorial
from math import sqrt, log, pow



def square_root(x):
    return sqrt(x)

def fact(x):
    return factorial(x)


def nat_log(x):
    return log(x)

def power(x,y):
    return pow(x,y)


if(__name__ == "__main__"):
    print("Welcome to the Calulator App \n")
    e = True
    while(e):
        print("enter your choice \n")
        print("1. Square root \n2. Factorial \n3. Natural Log \n4. Power function \n5. Quit")
        i = input()
        if(i == "5"):
            e = False
        elif(i == "1"):
            print("enter a number ")
            x = int(input())
            square_root(x)
        elif(i == "2"):
            print("enter a number ")
            x = int(input())
            fact(x)
        elif(i == "3"):
            print("enter a number ")
            x = int(input())
            nat_log(x)
        elif(i == "4"):
            print("enter x and y such that x^y ")
            x, y = input().split()
            power(int(x),int(y))
        