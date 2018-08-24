from turtle import *
pensize(4)
size = 20
for i in range(5):
    penup()
    backward(10)
    right(90)
    forward(10)
    left(90)
    pendown()
    for j in range(4):
        forward(size)
        left(90)
    size +=20

mainloop()