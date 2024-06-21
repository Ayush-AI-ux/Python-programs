# NL=["a","b","c",2,4,6,7,8]
# print(NL[3])
# print(NL[-1])
# list1=(NL[1:5])
# print(list1)
# NL[2]=10
# NL.append(20)
# del NL[0]
# NL.insert(1, 5)
# print(NL)

# list=[]
# N=int(input("Enter input to be add in list: "))
# for i in range(N):
#     item=input(f"Enter item {i+1}:")
#     list.append(item)


# print(f"finallist: {list}")

# list=[]
# N=int(input("Enter input to be add in list: "))
# for i in range(N):
#     item=int(input(f"Enter item {i+1}:"))
#     list.append(item)


# print(f"finallist: {list}")

# list =[2,4,5,1,6]
# print(max(list))

# list=[2,4,6,5,2]
# sum=0
# for i in list:
#     sum += i

# print(sum)

# list=[]
# N=int(input("Enter input to be add in list: "))
# for i in range(N):
#     item=int(input(f"Enter item {i+1}:"))
#     list.append(item)

# print(f"finallist: {list}")
# max_element =list[0]
# for i in list:
#     if i>max_element:
#         max_element=i
# print(f"Max element is: {max_element}")


# list=[1,2,3,4,5,6,7,8,3,2,2,2,2]
# element_to_count=3
# count=0

# for num in list:
#     if num==element_to_count:
#         count+=1

# print(f"The element{element_to_count} occurs {count} times")
# list=[]
# N=int(input("Enter number of input to be add in list: "))
# for i in range(N):
#     item=int(input(f"Enter item {i+1}:"))
#     list.append(item)
#     count=0
#     for j in range(len(list)):
#         if list[j]==item:
#             count+=1
#             pass
#         else:
#             print("No two element are same.")

# print(f"The element {item} occurs {count} times in list.")

# print("[" , end="")
# list=[1,2,3,4,5,6,7,8]
# for i in list[::-1]:
#     print(i,end=",")
# print("]")


# list=[]
# N=int(input("Enter number of input to be add in list: "))
# for i in range(N):
#     item=int(input(f"Enter item {i+1}:"))
#     list.append(item)

# print("Final_list:", list)
# reversed_list=[]

# for i in range(len(list) -1,-1,-1):
#     reversed_list.append(list)

# print(f"{reversed_list}")



# list=[]
# N=int(input("Enter number of input to be add in list: "))
# for i in range(N):
#     item=int(input(f"Enter item {i+1}:"))
#     list.append(item)

#     max_element=list[0]
#     for j in list:
#         if j>max_element:
#             max_element=j
#             # second_largest_element=i
#             for i in list:
#                 if i>max_element and i<j:
#                     second_largest_element=i

# print(f"Second largest element= {second_largest_element}")
# for i in list(8,1,-1):
#     print


# list=[]
# N=int(input("Enter number of input to be add in list: "))
# for i in range(N):
#     item=int(input(f"Enter item {i+1}:"))
#     list.append(item)
# unique_list=[]
# for j in list:
#     if j==item:
#         unique_list=list.remove(item)

# print(f"new_list= {unique_list}")

# list=[]
# N=int(input("Enter number of input to be add in list: "))
# for i in range(N):
#     item=int(input(f"Enter item {i+1}:"))
#     list.append(item)
# unique_list=[]
# for num in list:
#     if num not in unique_list:
#         unique_list.append(num)

# print(f"The list after removing duplicates is : {unique_list}")




# list1=[1,2,3,4,5]
# list2=[6,7,8,9,10]
# list3 =list1+list2
# print(list3)


# list=[]
# N=int(input("Enter input to be add in list: "))
# for i in range(N):
#     item=int(input(f"Enter item {i+1}:"))
#     list.append(item)

# smallest_element =list[0]
# for i in list:
#     if i<smallest_element:
#         smallest_element=i
# print(f"Smallest element is: {smallest_element}")


# a=str(input("Enter a: "))
# b=str(input("Enter b: "))
# c=''.join(reversed(a))
# if c==b:
#     print("True")
# else:
#     print("False")

# a=str(input("Enter a: "))
# b=str(input("Enter b: "))
# for i in a:
#     for j in b(-1):
#         if i==j:
#             print("True")

# a=int(input("Enter number: "))
# b=1
# for i in range(1,a+1):
#     b*=i
# print(f"Factorial of given number: {b}")
     
# squares = [x**2 for x in range(5)]
# print(squares)

# even_numbers = [x for x in range(10) if x%2==0]
# print(even_numbers)

# results = ['Pass' if score >= 60 else 'Fail' for score in [75, 30, 85, 50]]
# print(results)

# names = ['Jhon', 'Ayush', 'Gouransh']
# name_lengths = [len(name) for name in names]
# print(name_lengths)


# list =eval(input("Enter items of list: "))
# print(list)
# sum_even =0
# sum_odd=0
# for i in list:
#     if i%2==0:
#         sum_even += i
#     else:
#         sum_odd += i

# print(f"Sum of even numbers in list: ",sum_even)
# print(f"Sum of odd numbers in list: ",sum_odd)

# list =eval(input("Enter items of list: "))
# print(list)
# sum_even =0
# sum_odd=0
# for i in list:
#     if i%2==0:
#         sum_even += i**2
#     else:
#         sum_odd += i**3

# print(f"Sum of even numbers in list: ",sum_even)
# print(f"Sum of odd numbers in list: ",sum_odd)


# list = eval(input("Enter items to form a list: "))
# # num=int(input(f"Enter which largest element you want:"))
# max_element=list[0]
# l=[]
# for i in list:
#     if i>max_element:
#         max_element=i
#         l.append(max_element)
    
# print("l")

# N = int(input("Enter your ending number: "))
# for i in range(5, N+1, 5):
#     out = i+2
#     print(f"for {i} - {out}")


# num = input("Enter the number: ")
# l =[]
# for i in num:
#     l.append(i)
# sum = 0
# print(l)
# for j in l:
#     sum += int(j)
# print(sum)

# n=input("Enter any numbers-: ")
# a=0
# for i in n:
#     a=a+int(i)
# print(a)


# if __name__ == '__main__':
#     n = int(input().strip())
#     if n%2==1:
#         print("Weird")
#     elif n%2==0 and 2<=n<=5:
#         print("Not weird")
#     elif n%2==0 and 6<=n<=20:
#         print("Weird")
#     else:
#         print("Not weird")

# age = int(input("Enter your age: "))
# if age <= 3:
#  ticket_price = 0
# elif age <= 12:
#  ticket_price = 10
# elif age <= 17:
#  ticket_price = 15
# else:
#  ticket_price = 20
# print(f"The ticket price is: ${ticket_price}")


# import random
# target_number = random.randint(1, 100)
# while True:
#  user_guess = int(input("Guess the number (1-100): "))
#  if user_guess < target_number:
#     print("Too low. Try again.")
#  elif user_guess > target_number:
#     print("Too high. Try again.")
#  else:
#     print("Congratulations! You guessed the number.")
#     break
 
# n = int(input("Enter the number of rows: "))
# for i in range(1, n + 1):
#     print("*" * i)


# sentence = input("Enter a sentence: ")
# cs = sentence.title()
# print("Capitalized sentence:", cs)

# sentence = input("Enter a sentence: ")
# words = sentence.split()
# for word in words:
#     print(f"Length of '{word}': {len(word)}")


# import math
# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))
# sum_of_square_roots = math.sqrt(num1) + math.sqrt(num2)
# print("Sum of square roots:", sum_of_square_roots)


# import math
# radius = float(input("Enter the radius of the circle: "))
# area = math.pi * radius ** 2
# print(f"The area of the circle is: {area:.2f}")


# list1 = ["a", "b" , "c"]
# list2 = [1, 2, 3]
# for x in list2:
#  list1.append(x)
# print(list1)

# myData1 = ["orange", "mango", "kiwi", "pineapple", "banana"]
# myData1.sort()
# print(myData1)

# myData1 = ["a", "b", "c"]
# for i in range(len(myData1)):
#     print(myData1[i])

# veg = ["cabbage", "potato", "brinjal", "tomato"]
# newlist = []
# for x in veg:
#  if "o" in x:
#     newlist.append(x)
# print(newlist)

# n = input("Enter brackets:" )

# l = eval(input("Enter items: "))
# print(max(l))

# a=input()
# st=""
# for i in a:
#     if i=="(":
#         c=")"
#         st+=c
#     else:
#         d="(" 
#         st+=d
# print(st[::-1])
# if st[::-1]==a:
#     print("True")
# else:
#     print("false")

a = lambda x: x%3!=0 and str(x)[-1] !="3"
l=[]
n=int(input("enter your number :"))
i=1
while len(l)!=n:
    
    if a(i)==True:
        l.append(i)

    i+=1
print(l[-1])






