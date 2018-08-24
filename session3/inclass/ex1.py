#1 1st solution
print("1st solution")
for i in range (3):
    for j in range (4):
        print("x", end = " ")
    print()    
print()

#2 2nd solution
print("2nd solution")
print('''x x x x
x x x x
x x x x''')
print()

#3 3rd solution:
print("3rd solution")
for i in range(3):
    print("x x x x")
print()

#4 4th solution
print("4th solution")
g = ""
for i in range(4):
    g += "x "
for i in range (3):
    print(g)
print()