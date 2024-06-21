veg = str(input("Enter type of food you eat:"))
Budget = int(input("Enter your budget in $:"))
Time = int(input("How much time can you wait in minutes:"))
if veg == "v" and Budget == 10 and Time == 5:
    print("Thankyou for waiting 5 minutes .")
    print("We will offer you veg maggi.")
elif veg == "v" and Budget == 10 and Time == 10:
    print("Thankyou for waiting 10 minutes .")
    print("We will offer you veg burger.")
elif veg == "nv" and Budget == 10 and Time == 10:
    print("Thankyou for waiting 10 minutes .")
    print("We will offer you non veg burger.")
elif veg == "nv" and Budget == 20 and Time == 10:
    print("Thankyou for waiting 10 minutes .")
    print("We will offer you non veg pizza.")
elif veg == "v" and Budget == 20 and Time == 10:
    print("Thankyou for waiting 10 minutes .")
    print("We will offer you veg pizza.")
elif veg == "v" and Budget == 20 and Time == 20:
    print("Thankyou for waiting 20 minutes .")
    print("We will offer you veg sandwich.")
elif veg == "nv" and Budget == 20 and Time == 20:
    print("Thankyou for waiting 20 minutes .")
    print("We will offer you non veg plain sauce chapati .")
elif veg == "nv" and Budget == 30 and Time == 20:
    print("Thankyou for waiting 20 minutes .")
    print("We will offer you non veg cheese pizza.")
elif veg == "v" and Budget == 30 and Time == 20:
    print("Thankyou for waiting 20 minutes .")
    print("We will offer you veg cheese pizza.")
elif veg == "v" and Budget == 100 and Time == 10:
    print("Thankyou for waiting 10 minutes and for ordering most expensive food.")
    print("We will offer you veg paneer cheese pizza with vegetables.")
elif veg == "nv" and Budget == 100 and Time == 10:
    print("Thankyou for waiting 10 minutes and for ordering most expensive food.")
    print("We will offer you non veg cheese paneer burger with full vegeables.")
else:
    print("You had entered other data than menu.")
    print("Please enter your order according to menu.")