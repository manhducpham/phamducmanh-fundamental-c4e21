### serious exercise 4 part b

print("b. n stars:")
n_b = int(input("Please enter the number of stars "))

# 1st solution:
print("1st solution")
b = ""
for i in range(n_b):
    b += "* "
print(b)
print()

# 2nd solution:
print("2nd solution")
for i in range(n_b):
    print("*", end = " ")
print()
print()