post = "hi harry, this is the post which i am sending to you for your health, i hope you well"

# name = input("Enter the name:- ")
name = input("enter you name:- ")

if name in post:
    print(f"Yes this post is related to {name}")
else:
    print(f"No this post is not related to {name}")