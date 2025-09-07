#print the sum of all even and odd num in a range separately
n = int(input("Enter a number: "))
num = 0
num1= 0
for n in range(0, n+1):
    if(n %2 ==0): 
       num += n
    else:
         num1 += n
        

print(num)
print(num1)