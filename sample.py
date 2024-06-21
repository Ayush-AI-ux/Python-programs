# x="this is not none"
# try:
#   print(x)
# except NameError:
#   print("Variable x is not defined")
# except:
#   print("Something else went wrong")

# def prod (a, b):
#  return a*b

# result = prod(7, 3)
# print(result)

# numbers = [1, 20, 13, 10, 5, 6, 7]
# cmpl = [complex(x) for x in numbers if x < 10]
# print(cmpl)

# a = "hello"3
# hello = "a"
# print(eval(eval(eval(a))))

# text = "Python is great"
# result = text[0:-4:2]
# print(result)

# a="1"
# print(ord(a))


# values = "1234567"
# result = max(map(ord, values))
# print(result)

# file_name = 'data.txt'
# with open(file_name, 'r') as file:
#     contents = file.readlines()
#     print(len(contents))

# def Pr(num):
#     return ('Prime' if num % i != 0 for i in range(2, int(num**0.5) + 1) and num > 1 else 'Not prime')    

# n = int(input())
# re = Pr(n)
# print(re)

# def LeapYear(year):
#     return  ("LeapYear"*(year%4 ==0 or year%400 == 0 and year%100 == 0) + (year%4 != 0)*"Not leap year")


# n = int(input())
# re = LeapYear (n)
# print(re)

# import numpy as np
# xs = [12, 35, 67] 
# ys = [55, 86, 109] 
# plt.scatter(xs,ys)
# plt.show()