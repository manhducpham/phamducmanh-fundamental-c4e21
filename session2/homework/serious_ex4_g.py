### serious exercise 4 part g
print("g. n x m stars")
n_g = int(input("Please enter the number of stars in a row: "))
m_g = int(input("Please enter the number of rows: "))

# 1st solution
print("1st solution")
g = ""
for i in range(n_g):
    g += "* "
for i in range (m_g):
    print(g)
print()

# 2nd solution
print("2nd solution")
for i in range(m_g):
    for j in range (n_g):
        print("*", end = " ")
    print()
print()