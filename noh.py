def facto(n):
    x=1
    for i in range(1,n+1):
        x*=i
    return x
    
a=int(input("Enter a:"))
print(facto(a)/(facto(a-2)*facto(2)))

