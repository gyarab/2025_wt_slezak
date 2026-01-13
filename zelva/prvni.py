from turtle import forward, left, right, goto
from math import sqrt
from random import randint

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
    a = randint(30,40)
    c = sqrt(2*a**2)
    dum(a,c)
    right(60)
goto(0,0)#dokončí kruh "planety", aby tam nebyla mezera 
    
