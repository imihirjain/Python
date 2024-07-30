# def centi(inch):
#     return 2.54*inch

# num = int(input("Enter the number:- "))
# res= centi(num)
# print(res)


def inch(centi):
    return (centi/2.54)

num = int(input("Enter the number:- "))
res= inch(num)
print(res)