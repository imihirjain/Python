def greatest(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>c):
        return b
    else:
        return c

a = int(input("enter the first number:- "))
b = int(input("enter the second number:- "))
c = int(input("enter the third number:- "))
res = greatest(a,b,c)
print(res)