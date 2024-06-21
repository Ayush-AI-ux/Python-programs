import random 
target_value = random.randint(1,100)

while True:
    num=int(input("Enter your guessed value:"))

    if num<target_value:
        print("Enter a greater number")
    elif num>target_value:
        print("Enter a lesser number")
    
    else:
        print("Congratualtions!!, you guessed correctly.")
        break