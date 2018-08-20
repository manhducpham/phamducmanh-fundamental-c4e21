### serious exercise 4 part d
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
print()