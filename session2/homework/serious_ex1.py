weight = float(input("Please enter your weight in kg: "))
height = float(input("Please enter your height in cm: "))
height_m = height / 100
bmi = weight / (height_m**2)

if bmi < 16:
    conclusion = "severely underweight."
elif bmi < 18.5:
    conclusion = "underweight."
elif bmi < 25:
    conclusion = "normal."
elif bmi < 30:
    conclusion = "overweight."
else:
    conclusion = "obese."

print("Your BMI is", bmi, ". Based on your BMI, you are", conclusion)