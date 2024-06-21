# number1 = int(input("Enter start number of range:"))
# number2 = int(input("Enter stop number of range:"))
# for number in range ((number1),(number2),1):
#     if number % 2 == 0:
#         print(number,"is even")
#     else:
#         print(number,"is odd")

even = []
odd = []
num1 = int(input("Enter start number of range:"))
num2 = int(input("Enter stop number of range:"))
for i in range (num1,num2):
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print("even = ",even,"\n","odd = ",odd)  
