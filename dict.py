# md={
#     "University":"GLA",
#     "Location":"Mathura",
#     "Year":1998
# }
# print(md)

# md={
#     "University":"GLA",
#     "Location":"Mathura",
#     "Year":1998
# }
# print(md["University"])

# md={
#     "University":"GLA",
#     "Location":"Mathura",
#     "Year":1998,
#     "Year":1996
# }
# print(md)
# print(len(md))
# print(type(md))

# md={
#     "University":"GLA",
#     "Location":"Mathura",
#     "Year":1998,
#     "color":["red","blue","pink"]
# }
# print(md)


# datad=dict(name="Ayush",age=18,country="India")
# print(datad)

# md={
#     "University":"GLA",
#     "Location":"Mathura",
#     "Year":1998
# }

# check=md["Year"]
# print(check)

# x=md.get("Year")
# print(x)

# x1=md.keys()
# print(x1)

# x2=md.values()
# print(x2)

# car={
#     "brand":"Safari",
#     "model":"Mustang",
#     "year":3234
# }
# x=car.keys()
# print(x)

# car["color"]:"white"
# print(car)
# print(x)

# td={
#     "brand":"Ford",
#     "model":"Mustang",
#     "year":2023
# }

# x=td.items()
# print(td)
# print(x)

# td={
#     "brand":"Ford",
#     "model":"Mustang",
#     "year":2023
# }
# if "model" in td:
#     print("Yes,'model' is one of the keys in this td dictionary")

# MD={
#     "university":"GLAU",
#     "Location":"Mathura",
#     "year":2020
# }
# MD["year"]=2023
# print(MD)

# MD={
#     "university":"GLAU",
#     "Location":"Mathura",
#     "year":1964
# }
# MD.update({"year":2020})
# print(MD)

# MD={
#     "university":"GLAU",
#     "Location":"Mathura",
#     "year":1964
# }
# for x in MD:
#     print(x)

# for x in MD:
#     print(MD[x])

# for x in MD.values():
#     print(x)

# for x in MD.keys():
#     print(x)

# for x, y in MD.items():
#     print(x, y)


# MD={
#     "university":"GLAU",
#     "Location":"Mathura",
#     "year":1964
# }
# MD.pop("Location")
# print(MD)

# MD.popitem()
# print(MD)

# del MD["year"]
# print(MD)

# del MD
# print(MD)

# MD.clear()
# print(MD)

# List=eval(input("Enter items"))
# print(List)

# Dict=eval(input("Enter dictionary item"))
# print(Dict)

# user_dict={}
# num_pairs=int(input("Enter number of key-value pairs you want to add: "))

# for x in range(num_pairs):
#     key=input("Enter the key: ")
#     value=input("Enter the value: ")
#     user_dict[key]=value

# print("Resulting dictionary: ")
# print(user_dict)    

# myS={
#     "stud1": {
#         "name":"Sachin",
#         "year":2004
#     },
#     "stud2": {
#         "name":"Laxman",
#         "year":2007
#     },
#     "stud3": {
#         "name":"Ram",
#         "year": 2011
#     }
# }
# print(myS)

# for x in myS:
#     print(x)

# print(myS["stud2"]["name"])

# Dict={
#     "John":85,
#     "Jane":90,
#     "Bob":75,
#     "Alice":95
# }
# Dict["Sam"]=80
# Dict.update({"Bob":80})
# Dict["Bob"]=80
# del Dict["Jane"]

# for name, score in Dict.items():
#     print(f"{name}:{score}")

# inv={
#     "apple":10,
#     "banana":5,
#     "orange":8,
#     "grape":3
#     }
# inv.update({"apple":12})
# if 'banana' in inv:
#     print("Banana is in inventory.")
# else:
#     print("Banana not in inventory")
# inv.update({"grape":2})
# print(inv)
# ti=sum(inv.values())
# print(f"Total values in inventory: {ti}")

Los={
    "John":30,
    "Aohn":45,
    "Bohn":54,
    "Cohn":42
}
max_num=-1
for x in Los.values():
    if x > max_num:
        max_num=x

top_students=[student for student, x in Los.items() if x==max_num]

print(f"The highest grade is: {max_num}")
print(f"The student(s) with the highest grade: {','.join(top_students)}")














