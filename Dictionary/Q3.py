#count the frequency of elemnt in dict

l = [1, 2, 2, 3, 4, 4, 4, 5]
freq = {}
for item in l:
    if item in freq:
        freq[item] += 1  
    else:
        freq[item] = 1  

print(freq)
