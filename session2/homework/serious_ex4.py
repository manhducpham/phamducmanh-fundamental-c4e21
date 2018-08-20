### a

n_a = 20
print("a.", n_a, "x 1 stars:")

# 1st solution:
a = ""
for i in range (n_a):
    a += "* "
print(a)
print()

# 2nd solution:
for i in range(n_a):
    print("*", end = " ")
print()

### b

print("b. n stars:")
n_b = int(input("Please enter the number of stars "))

# 1st solution:
b = ""
for i in range(n_b):
    b += "* "
print(b)
print()

# 2nd solution:
for i in range(n_b):
    print("*", end = " ")
print()

### c

n_c = 9
print("c.", n_c, "stars and xs in total:")

# 1st solution:
c = ""
for i in range(n_c):
    if i%2 == 0:
        c += "x "
    else:
        c += "* "
print(c)
print()

# 2nd solution:
for i in range(n_c // 2):
    print("x *", end = " ")
if n_c % 2 == 1:
    print("x")
print()

### d
print("d. n stars and xs in total:")
n_d = int(input("Please enter a number: "))

# 1st solution:
d = ""
for i in range(n_d):
    if i%2 == 0:
        d += "x "
    else:
        d += "* "
print(d)
print()

# 2nd solution:
for i in range(n_d // 2):
    print("x *", end = " ")
if n_d % 2 == 1:
    print("x")
print()

### e
print("e. Use print() to move a new line:")
print()

### f
n_f = 7
m_f = 3
print("f.", n_f, "x", m_f, "stars")

# 1st solution
f = ""
for i in range(n_f):
    f += "* "
for i in range (m_f):
    print(f)
print()

# 2nd solution
for i in range(m_f):
    for j in range (n_f):
        print("*", end = " ")
    print()
print()

### g
print("g. n x m stars")
n_g = int(input("Please enter the number of stars in a row: "))
m_g = int(input("Please enter the number of rows: "))

# 1st solution
g = ""
for i in range(n_g):
    g += "* "
for i in range (m_g):
    print(g)
print()

# 2nd solution
for i in range(m_g):
    for j in range (n_g):
        print("*", end = " ")
    print()
print()