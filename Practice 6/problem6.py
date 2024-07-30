marks = int(input("Enter your marks:- "))

if(marks>=90 and marks<100):
    print(f"{marks}, Ex")
elif(marks>=80 and marks<90):
    print(f"{marks}, A")
elif(marks>=70 and marks<80):
    print(f"{marks}, B")
elif(marks>=60 and marks<70):
    print(f"{marks}, C")
elif(marks>=50 and marks<60):
    print(f"{marks}, D")
else:
    print(f"{marks}, F")