n = int(input("Please enter the number of angles: "))

from turtle import *
shape("turtle")
# background("lightgreen")

for i in range(n):
    forward(100)
    left(360/n)

mainloop()