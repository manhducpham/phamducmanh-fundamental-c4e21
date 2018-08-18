from turtle import *

# shape("turtle")
speed(0)

#draw rectangle
penup()
setx(-200)
sety(150)

pendown()
begin_fill()
fillcolor("yellow")
for i in range(4):
    forward(100)
    left(90)
end_fill()

#draw triangle
penup()
setx(100)
sety(150)

pendown()
begin_fill()
fillcolor("yellow")
for i in range(3):
    forward(100)
    left(120)

end_fill()
#draw circle
penup()
setx(-150)
sety(-150)

pendown()
begin_fill()
fillcolor("yellow")

circle(50)

end_fill()

#draw multiple circles
fillcolor("black")
penup()
setx(150)
sety(-150)

pendown()
for i in range(36):
    circle(50)
    left(10)


mainloop()