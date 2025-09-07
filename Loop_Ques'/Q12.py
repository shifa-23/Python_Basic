n = input("Enter a word: ")
is_palindrome = True
length = len(n)

for i in range(length // 2):  
    if n[i] != n[length - 1 - i]:
        is_palindrome = False
        break

if is_palindrome:
    print("Palindrome")
else:
    print("Not a palindrome")
