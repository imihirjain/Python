import random
'''
1s
0w
-1g
'''

computer = random.choice([1,0,-1])
yourChoice = input("Enter your choice:- ")
youDict = {"s":1, "w":0, "g":-1}
reverseDict = {1:"snake", 0:"water", -1:"gun"}

you = youDict[yourChoice]

print(f"Your choice is:- {reverseDict[you]}\nComputer choice is:- {reverseDict[computer]}")

if(computer==you):
    print("It's a tie!")
else:
    if(computer == 1 and you==-1):
        print("You Win!")
    elif(computer == 1 and you==0):
        print("You Lose!")
    elif(computer == 0 and you ==-1):
        print("You Lose!")
    elif(computer == 0 and you==1):
        print("You Win!")
    elif(computer == -1 and you==1):
        print("You Lose!")
    elif(computer == -1 and you==0):
        print("You Win!")
    else:
        print("Invalid input!")