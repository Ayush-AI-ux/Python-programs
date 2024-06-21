# st=int(input("Enter starting number:"))
# en=int(input("Enter ending number:"))
# mult=1
# for i in range(st,en+1):
#     if i <= 20 and i > 0:
#         print(i)
#     else:
#         if i>20 and i % 2 == 0:
#             for j in range(1,i+1):
#                 mult = mult*j
#             print(mult)
#         else:
#             print(i)
            
# user_input = input("Enter the string ")
# data_alphabets = ""
# data_digits = ""
# for i in user_input:
#     if i.isalpha():
#         data_alphabets+=i
#     elif i.isdigit():
#         data_digits+=i
# print(f"All the digits are :- {data_digits}")
# print(f"All the alphabets are:- {data_alphabets}")

# i = 1
# while i < 10:
#   print(i)
#   i += 1
  
# input_word = "Hello"
# # Initialize a dictionary to store character counts
# char_count = {}
# # Iterate through each character in the input word
# for char in input_word:
#  if char in char_count:
#     char_count[char] += 1
#  else:
#     char_count[char] = 1
# # Print the character counts
# for char, count in char_count.items():
#     print(f"{char} : {count}")

        
# input_str = "aabcccccaaa"
# compressed_str = ""
# count = 1
# for i in range(len(input_str)-1):
#  if input_str[i] == input_str[i+1]:
#     count += 1
#  else:
#     compressed_str += input_str[i] + str(count)
#     count = 1
# compressed_str += input_str[-1] + str(count)
# print(compressed_str)

# names = ['John', 'Jane', 'Jim']
# name_lengths = [len(name) for name in names]
# print(name_lengths)


# num_elements = int(input("Enter the number of elements to add to the list: "))
# original_list = [0] * num_elements
# print("Original List:", original_list)
# for i in range(num_elements):
#  #element = int(input(f"Enter element {i+1}: "))
#  element = input(f"Enter element {i+1}: ")
#  original_list[i] = element
# print("Finally the list:", original_list)\
    
# my_list = [1, 2, 3, 4, 5]
# reversed_list = []
# for i in range(len(my_list) - 1, -1, -1):
#  reversed_list.append(my_list[i])
# print(f"The reversed list is: {reversed_list}")


# my_list = [1, 2, 3, 4, 5]
# reversed_list = []
# for i in my_list:
#     reversed_list[-1]=my_list[i]
    
# print(reversed_list)

# def my_function(fname):
#   print(fname + " Refsnes")

# my_function("Emil")
# my_function("Tobias")
# my_function("Linus")

# def my_function(fname, lname):
#   print(fname + " " + lname)

# my_function("Emil", "Refsnes")

# def my_function(*kids):
#   print("The youngest child is " + kids[1])

# my_function("Emil", "Tobias", "Linus")


# def my_function(child3, child2, child1):
#   print("The youngest child is " + child2)

# my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")



# import mymodule

# mymodule.greeting("Jonathan"
# try:
#   print(x)
# except:
#   print("An exception occurred")

# try:
#   print(x)
# except NameError:
#   print("Variable x is not defined")
# except:
#   print("Something else went wrong")

# try:
#   print("Hello")
# except:
#   print("Something went wrong")
# else:
#   print("Nothing went wrong")
x=10
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")