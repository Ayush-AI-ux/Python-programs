s1=int(input("Enter length of first side"))
s2=int(input("Enter length of second side"))
s3=int(input("Enter length of third side"))
if (s1 == s2) and (s2 == s3):
    print("Triangle is equilateral")
elif s1 == s2 or s3 == s2 or s1 == s3:
    print("Triangle is isosceles")
else:
    print("Triangle is scalene")
