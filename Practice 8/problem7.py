def remove(name, word):
    new_list=[]
    for item in name:
        if not(item==word):
            new_list.append(item.strip(word))
    return new_list   
    

name = ["harry", "rohan", "shubham", "an"]

print(remove(name,"an"))