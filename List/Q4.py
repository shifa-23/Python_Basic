# #2nd greatet

# l = [1, 2, 3, 4]
# max = l[0]
# index = 0

# for i in range(len(l)):
#     if l[i] > max:
#         # max = l[i]
#         index = i

# print(max)
# print(index)
l = [1, 2, 3, 4]

max1 = l[0]     
max2 = float()
index = 0

for i in range(len(l)):
    if l[i] > max1:
        max2 = max1
        max1 = l[i]
        index = i
    elif l[i] > max2 and l[i] != max1:
        max2 = l[i]

print("Second greatest:", max2)
