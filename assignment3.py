PA = int(input("Enter your purchase amount in $:"))
MEM = str(input("Are you member of our company:"))
if PA >= 100 and MEM=="yes":
    print("Total payable cost = ",PA-(PA*10)/100)
else:
    print("You can't get any discount.")
    print("Total payable cost =", PA)