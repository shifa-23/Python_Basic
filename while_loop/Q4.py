#num guessing
import random
num = int (input("ENter a number"))
a = random.randint(1,10)
if num == a :
    print(" you r right")
else:
    print("guess again")