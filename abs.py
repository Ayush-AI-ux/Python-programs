# n1 = int(input())
# n2 = int(input())
# c = n1*n2
# print(f"output {c}")

# n = int(input())
# d1 = int(input())
# if n%d1==0:
#     d2 = int(input())
#     if n%d2==0:
#         print("Yes.")
#     else:
#         print("No.")
# else:
#     print("No.")
# a=int(input())
# b=int(input())
# c=int(input())
# x =max(a,b,c)
# print(x)


# n = int(input())
# sum=0
# for i in range(1,n+1):
#     if i%2 ==0 and i%3==0:
#         sum+=i
#         print(sum)

# sentence = str(input())
# count=0
# for i in sentence:
#     if i in ("a","e","i","o","u","A","E","I","O","U"):
#         count+=1
# print(count)

# numbers = [int(i) for i in input("Enter a list of integers separated by spaces: ").split()]
# result=[x**2 for x in numbers if (x**2)%2 == 0]
# print(" ".join([str(x) for x in result]))

# a=input().split()
# print(a)
# b=int(a[0])
# c=int(a[1])
# k = int(input())
# d = b & c
# e = b | c
# f = b ^ c
# l=[]
# l.append(d)
# l.append(e)
# l.append(f)
# print(l)
# for i in range(0,len(l)):
#     m=max(l)
#     if m<k:
#         print(m)
#         break
#     else:
#         l.remove(m)

# n = input().split()
# for i in n:
#     if int(i)%2==0:
#         print(int(i)**2,end=" ")

# x = int(input())
# y = int(input())
# result = x if x>y else y
# print(result)

# is_r = input()
# activity = 'Stay Indoors'if is_r == "True" else 'Go for a walk'
# print(activity)

# number = eval(input())
# result = [x*2 if x%2==0 else x**2 for x in number]
# print(result)

# temp = int(input())
# result = ["Warm" if temp > 25 else "Cold"]
# print(result)

# numbers = eval(input())
# list=[]
# for x in numbers:
#     if x%2==0:
#      y = x**2
#      list.append(y)

# print(list)

# x = int(input())
# result = ["x is less than 10" if x<10 else "x is equal to 10" if x==10 else "x is greater than 10"]
# print(result)

# us_in = input("Enter number with spaces between them: ")
# numbers =list(map(int, us_in.split()))
# squared_numbers= list(map(lambda x : x**2 , numbers))
# print(f" Original Numbers: {numbers}")
# print(f"Squared Numbers: {squared_numbers}")


# num = input().split()
# print(num)
# for i in num:
#     if int(i)%3==0 and str(i)[-1]=="3":
#         list= num.remove(int(i))
# print(list2)



# u_in= input("Enter numbers separated by spaces:")
# numbers = list(map(int, u_in.split()))
# even_odd_checker= list(map(lambda x: "Even" if x%2==0 else "Odd", numbers))
# print("Results: ", even_odd_checker)


# myTuple = ("A","B","C")
# print(myTuple)

# myT1 = ("A","C","D","AD")
# print(myT1)
# print(len(myT1))
# print(type(myT1))

# tu1=(1,2,"B","D",32)
# tu2=(3,4,5,"S","H",53)
# tu3=("A",3,4,3.4,"f")
# print(tu1,tu2,tu3)


# tt=("A","B","C")
# for x in tt:
#     print(x*2)

# tt=("A","B","C")
# for i in range(len(tt)):
#     print(tt[i])

# tt=("A","B","C")
# i = 0
# while i < len(tt):
#     print(tt[i])
#     i = i +1

# ages=[1,2,3,4,5]
# print(ages[1+3])
# print(sum(ages))


# x=bin(54)[2:]
# print(x)

# d={
#     "name":"ayush",
#     "age":1,
#     "age":1,
#     "class":1
# }
# print(d)

# d={
#     "item1":200,
#     "item2":100,
#     "item3":300,
# }

# print("{")
# for i,j in d.items():
#     print(f"{i}:{j}")
# print("}")

# student=["ayush","aryan","gouransh"]
# marks=[28,29,30]
# d={}
# for i in range(0,len(student)+1):
#     for j in marks(0,len(marks)+1):
#         if student[i]==marks[j]:
#             print(f"{i}:{j}")
#         else:
#             break

# x = "Python "
# y = "is "
# z = "awesome"
# print(x + y + z)


# x = "awesome"

# def myfunc():
#   x = "fantastic"
#   print("Python is " + x)

# myfunc()

# print("Python is " + x)

# x = "awesome"

# def myfunc():
#   global x
#   x = "fantastic"

# myfunc()

# print("Python is " + x)

# x = 1.10
# y = 1.0
# z = -35.59

# print(type(x))
# print(type(y))
# print(type(z))

# a = "Hello, World!"
# print(a[1])

# try:
#   a=2
#   b=int(input("Enter"))
#   print(a+b)
# except Exception as e:
#   print("==> error",e)
# print(a)
# print(b)

# txt = "The best things in life are free!"
# print("free" in txt)

# txt = "The best things in life are free!"
# print("expensive" not in txt)

# b = "Hello, World!"
# print(b[0:-5:2])


# a = " Hello, World! "
# print(a.strip())


# age = 36
# print("My name is John, and I am {}".format(age))

# txt = "We are the so-called Vikings from the north."
# print(txt.count("h"))

# print(10 > 9)
# print(10 == 9)
# print(10 < 9)


# print(bool("Hello"))
# print(bool(15))

# x = "Hello"
# y = 15

# print(bool(x))
# print(bool(y))


# print(bool("abc"))
# print(bool(123))
# print(bool(["apple", "cherry", "banana"]))

# x = -200
# print(isinstance(x, int))

# n = int(input("Enter number: "))
# def prime():
#   return "Prime" if[i for i in range(2,n) if n % i == 0]==[] else "Not Prime"

# result= prime()
# print(result)


def LeapYear(year):
 return  "Leap Year"*(year%4 == 0 or year%400 == 0 and year%100 != 0 )+ "Not a leap year"*(year%4 !=0)


year = int(input())
re = LeapYear (year)
print(re)



# def check_status(a, b, flag):
#     return "True" if (a>0 or b>0) and flag == "false" or (a<0 and b<0) and flag=="true" else "False"
    
# a=int(input("Enter a: "))
# b = int(input("Enter b:"))
# flag = input("Enter true/false: ")
# result=check_status(a,b,flag)
# # print(result)

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[-4:-1])


# thislist = ["apple", "banana", "cherry"]
# thislist[1:3] = ["watermelon"]
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist.insert(2, "watermelon")
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# tropical = ["mango", "pineapple", "papaya"]
# thislist.extend(tropical)
# print(thislist)


# thislist = ["apple", "banana", "cherry"]
# thistuple = ("kiwi", "orange")
# thislist.extend(thistuple)
# print(thislist)


# thislist = ["apple", "banana", "cherry"]
# i = 0
# while i < len(thislist):
#   print(thislist[i])
#   i = i + 1


# def myfunc(n):
#   return abs(n - 50)

# thislist = [100, 50, 65, 82, 23]
# thislist.sort(key = myfunc)
# print(thislist)



# thistuple = ("apple", "banana", "cherry")
# y = ("orange",)
# thistuple += y

# print(thistuple)

# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

# (green, yellow, *red) = fruits

# print(green)
# print(yellow)
# print(red)

# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}

# x.intersection_update(y)

# print(x)


# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}

# z = x.intersection(y)

# print(z)


# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }

# x = car.keys()

# print(x) 

# car["color"] = "white"

# print(x) 


