while True:
    password = input("Create a password(at least 6 characters):")
    if len(password) < 6:
        print("Password is too short.Please try again.")
        pass
    else:
        print("Password set successfully.")
        break