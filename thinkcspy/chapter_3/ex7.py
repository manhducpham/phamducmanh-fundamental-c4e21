from turtle import *
# shape("heart")

penup()
for i in (160, -43, 270, -97, -43, 200, -940, 17, -86):
    stamp()
    forward(100)
    left(i)

mainloop()
