from turtle import *

def draw_poly(n, sz):
    for i in range(n):
        forward(sz)
        left(360 / n)

draw_poly(8, 50)

mainloop()