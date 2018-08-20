### serious exercise 4 part c

n_c = 9
print("c.", n_c, "stars and xs in total:")

# 1st solution:
print("1st solution")
c = ""
for i in range(n_c):
    if i%2 == 0:
        c += "x "
    else:
        c += "* "
print(c)
print()

# 2nd solution:
print("2nd solution")
for i in range(n_c // 2):
    print("x *", end = " ")
if n_c % 2 == 1:
    print("x")
print()
print()