'''
1   rock
0   paper
-1  scisor
'''

import random
computer = random.choice([1,0,-1])
yourChoice = input("Enter Your Choice:- ")
dict = {"r":1, "p":0, "s":-1}
reverseDict = {1:"Rock", 0:"Paper", -1:"Scissor"}
you = dict[yourChoice]

print(f"Your choice is:- {reverseDict[you]}\nComputer choice is:- {reverseDict[computer]}")

if(computer == you):
    print("It is a tie!")
else:
    if(computer == 1 and you == 0):
        print("You Win")
    elif(computer == 1 and you == -1):
        print("Computer Win")
    elif(computer == 0 and you == 1):
        print("Computer Win")
    elif(computer == 0 and you == -1):
        print("You Win")
    elif(computer == -1 and you == 1):
        print("You Win")
    elif(computer == -1 and you == 0):
        print("Computer Win")
    else:
        print("Invalid Input")