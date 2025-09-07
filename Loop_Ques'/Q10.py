#prime num

n = int(input("Enter a number: "))

for i in range(2, int(n**0.5) + 1):  
        if n % i == 0:
            print("not prime")
        else:
              print("Prime")