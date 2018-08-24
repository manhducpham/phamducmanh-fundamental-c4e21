m = int(input("enter the number of x in a row (m): "))
n = int(input("enter the number of rows (n): "))

#1 1st solution
print("1st solution")
for i in range (n):
    for j in range (m):
        print("x", end = " ")
    print()    
print()
#2 2nd solution
print("2nd solution")
for i in range(n):
    print("x " * m)
print()
