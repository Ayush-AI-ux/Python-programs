list=[]
while True:
    print("==========ENHANCED CALCULATOR===========")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4.Division")
    print("5.Display operations")
    print("6. Quit")
    print("========================================")
    Choice = int(input("Enter your choice(1/2/3/4/5/6): "))
    if Choice == 1:
        First = int(input("Enter first number: "))
        Second = int(input("Enter second number: "))
        a=(First+Second)
        print(f"{First} + {Second} = {a}")
        list.append(f"{First} + {Second} = {a}")
    elif Choice==2:
        First = int(input("Enter first number: "))
        Second = int(input("Enter second number: "))
        b=(First-Second)
        print(f"{First} - {Second} = {b}")
        list.append(f"{First} - {Second} = {b}")
    elif Choice==3:
        First = int(input("Enter first number: "))
        Second = int(input("Enter second number: "))
        c=(First*Second)
        print(f"{First} * {Second} = {c}")
        list.append(f"{First} * {Second} = {c}")
    elif Choice==4:
        First = int(input("Enter first number: "))
        Second = int(input("Enter second number: "))
        d=(First/Second)
        print(f"{First} / {Second} = {d}")
        list.append(f"{First} / {Second} = {d}")
    elif Choice==5:
        print("==============Display Operations==============")
        for i,list in enumerate(list, start=1):
            print(f"{i}. {list}")
        print("==============================================")
    else:
        break
