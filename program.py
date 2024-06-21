a=int(input("Enter number one"))
b=int(input("Enter number second"))
if (a < 0) and (b > 0) :
    print("Enter the positive value of a")
elif (a > 0) and (b < 0) :
    print("Enter the positive value of b")
else :
     d=str(input("Enter the operator for calculation"))

if d=="+":
    print("The addition of two numbers", a+b)
elif d=="-":
    print("The subtraction of two numbers", a-b)
elif d=="/":
    print("The division of two numbers", a/b)
elif d=="*":
    print("The multiplication of two numbers", a*b)
elif d=="//":
    print("The floor division of two numbers", a//b)
elif d=="**":
    print("The exponential of two numbers", a**b)
elif d=="%":
    print("The modulus of two numbers", a%b)
else:
    print("You have entered a wrong operator ")
    print("Please reenter correct operator")