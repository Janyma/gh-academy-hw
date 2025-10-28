
import random


def guesser(c):
    a=random.randint(1,100)
    while(c>0):
        b=int(input("guess number: "))

        if (b>a):
            print("Too high")
            c-=1
        if(b<a):
            print("Too low")
            c-=1
        if(a==b):
            a="Correct"
            return a

print(guesser(5))


    