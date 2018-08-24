yob = int(input("Your year of birth? "))
now = 2018
age = now - yob
# a = str(age)
print("Your age is", age)

if age < 10:
    print("Baby")
elif age < 18: #else if
    print("Teenager")
else:
    print("Adult")