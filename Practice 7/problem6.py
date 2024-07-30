n = int(input("Enter the number:- "))
prod=1
# using for loop
# for i in range(1,n+1):
#     prod *=i

# print(prod)

# using while loop
i=1
while(i<=n):
    prod *=i
    i +=1
print(prod) 