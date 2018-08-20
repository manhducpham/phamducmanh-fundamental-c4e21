from turtle import *

shape("turtle")
speed(0)
title("turtle exercise 1")
pencolor("red")
pensize(2)

right(30)
for i in range (4):
    forward(100)
    left(60)
    forward(100)
    left(120)
    forward(100)
    left(60)
    forward(100)
    right(150)

mainloop()