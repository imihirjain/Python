def farhanheit(cel):
    f=(cel * 9/5) + 32
    return f

def celsius(farh):
    c=(farh - 32) * 5/9
    return c

cels = int(input("enter the celsius:- "))
farhe = float(input("enter the farhanheit:- "))
result = farhanheit(cels)
result1 = celsius(farhe)
print(result)
print(result1)