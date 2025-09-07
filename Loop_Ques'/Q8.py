#print the factor of a  num
#print the sum of all even and odd num in a range separately
n = int(input("Enter a number: "))
for i in range(1, n+1):
    if(n% i ==0):
        print(i, end = "")
        print()

