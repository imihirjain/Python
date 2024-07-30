# sum of n natural number
# using function
# def natural(n):
#     sum=0
#     for i in range(1,n+1):
#         sum = sum+i
#     return sum
# num = int(input("Enter the number:- "))
# result = natural(num)
# print(result)

# using recursion
def natural(n):
    if(n==0):
        return 0
    return n+natural(n-1)

num = int(input("Enter the number:- "))
result = natural(num)
print(result)