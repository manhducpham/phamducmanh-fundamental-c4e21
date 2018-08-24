from turtle import *
colors = ['red', 'blue', 'brown', 'yellow', 'grey']

speed(0)
title("turtle exercise 1")
pensize(2)

n_max = 7
n_min = 3

for i in range (n_min, n_max + 1):
    color_n = colors[i - 3]
    color(color_n)
    for t in range (i):
        forward(100)
        left(360 / i)

mainloop()