n = input("Enter a word: ")

symbol = 0
digit = 0
char = 0

for i in n:
    if i.isdigit():
        digit += 1
    elif i.isalpha():           
        char += 1
    else:                       
        symbol += 1
print("Digits:", digit)
print("Alphabets:", char)
print("Symbols:", symbol)
