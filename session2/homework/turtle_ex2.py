from turtle import *

shape("turtle")
speed(5)
title("turtle exercise 2")
pensize(1)

for i in range (3, 7):
    if i%2 == 0:
        pencolor("red")
    else:
        pencolor("blue")
    for t in range (i):
        forward(100)
        left(360 / i)

mainloop()