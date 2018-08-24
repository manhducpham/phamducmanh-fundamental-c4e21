from turtle import *
shape("turtle")
bgcolor("lightgreen")
color("blue")

for i in range(12):
    penup()
    forward(100)
    pendown()
    forward(10)
    penup()
    forward(25)
    stamp()
    backward(135)
    left(30)

mainloop()