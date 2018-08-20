### serious exercise 4 part f
n_f = 7
m_f = 3
print("f.", n_f, "x", m_f, "stars")

# 1st solution
print("1st solution")
f = ""
for i in range(n_f):
    f += "* "
for i in range (m_f):
    print(f)
print()

# 2nd solution
print("2nd solution")
for i in range(m_f):
    for j in range (n_f):
        print("*", end = " ")
    print()
print()