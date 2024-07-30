with open("poems.txt") as f:
    content=f.read()
    if("twinkle" in content):
        print("twinkle is present")
    else:
        print("twinkle is not present")