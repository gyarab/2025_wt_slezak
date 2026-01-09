from turtle import forward, left, right
from math import sqrt
from random import randint
a = randint(30,50)
c = sqrt(2*a**2)
def dum(a,c):
    for i in range(4):
        forward(a)
        left(90)
    left(45)
    forward(c)
    left(90)
    forward(c/2)
    left(90)
    forward(c/2)
    left(90)
    forward(c)
    left(45)
for i in range(6):
    dum(a,c)
    right(60)
    
