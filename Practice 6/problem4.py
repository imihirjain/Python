username = input("Enter your username:- ")

user_length = len(username)

if(user_length < 10):
    print(f"{username} has less than 10 character")
elif(user_length==10):
    print(f"{username} has equal to 10 character")
else:
    print(f"{username} has more than 10 character")