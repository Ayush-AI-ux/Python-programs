num1 = float(input("Enter first number:"))
num2 = float(input("Enter second number:"))
if (num1 > 0 and num2 == 0) or (num1 < 0 and num2 < 0) or (num1 < 1 and num2 < 1) or (num1 == 0 and num2 == 0) or (num1 == 0 and num2 > 0):
    print("Invalid")
elif (num1 > 0 and num2 > 0) and num1 > num2:
    print("Number 1 is largest")
elif (num1 > 0 and num2 > 0) and num1 < num2:
    print("Number 2 is largest")
else:
    print("Both values are same ,please enter new numbers.")
    