Weight = int(input("Enter your weight in kg:"))
Height = float(input("Enter your height in meters:"))
BMI = Weight/(Height**2)
print("Your BMI is:", Weight/(Height**2))
if BMI < 18.5:
    print("You are underweight.")
elif BMI < 25:
    print("You are normal.")
elif BMI < 30:
    print("You are overweight.")
else:
    print("You are obese.")