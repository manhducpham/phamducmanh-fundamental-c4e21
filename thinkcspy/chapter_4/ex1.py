from turtle import *
bgcolor("lightgreen")
color("pink")
speed(9)
pensize(3)
penup()
backward(200)
pendown()


for i in range(5):
    for j in range(4):
        forward(40)
        left(90)
    penup()
    forward(69)
    pendown()

mainloop()