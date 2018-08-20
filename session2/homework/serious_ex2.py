n = int(input("Please enter a number: "))

#1 use loop
factorial_n = 1
for i in range(1, n+1):
    factorial_n *= i

#2 use factorial function
# import math
# factorial_n = math.factorial(n)

print("th factorial of", n, "is", factorial_n)
