# Replace placeholders with actual values
# name = input("enter your name:- ")

letter = '''Dear <|NAME|>,
        Your are selected!
        <|Date|>
    '''

print(letter.replace("<|NAME|>", "Mihir jain").replace("<|Date|>", "11-07-2024"))