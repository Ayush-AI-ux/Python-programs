GPA = float(input("Enter your GPA:"))
PEA = str(input("Had you participated in extracurricular activity?"))
if GPA >= 3.5 and PEA == "yes":
    print("You are eligible for scholarship.")
else:
    print("you are not eligible for scholarship.")