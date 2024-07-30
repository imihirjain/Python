comment = ["make a lot of money", "buy now", "subscribe this", "click this"]

user_comment = input("Enter your comment:- ")

if user_comment.lower() in comment:
    print("Spam comment")
else: 
    print("No spam comment")