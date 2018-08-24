from turtle import *

shape("turtle")
speed(0)
title("Maze")

# for i in range (1, 100):
#     forward(i*4)
#     left(90)
#cach khac
dist = 10
for i in range(1, 100):
    forward(dist)
    left(90)
    dist = dist + 5 # dist +=5


mainloop()