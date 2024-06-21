age = int(input("Enter your age"))
if age >= 18:
    print("You are eligible for vote")
    if age >= 21:
       print("You are also eligible for driving licence also")
else:
    print("You are not eligible for vote as well as driving licence")