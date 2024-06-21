while True:
    Age = int(input("Enter your age"))
    if Age < 0 or Age > 120:
       print("You had entered invalid age.Please enter correct age")
       pass
    else:
       print("Your age is checked")
       break