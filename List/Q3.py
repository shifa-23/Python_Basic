l = [1, 2, 3, 4]
max = l[0]
index = 0

for i in range(len(l)):
    if l[i] > max:
        max = l[i]
        index = i

print(max)
print(index)