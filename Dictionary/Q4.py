#combine two dic by adding values for commn key

dict1 = {"id1": "shifa", "id2": "she"}
dict2 = {"id2": "shi", "id3": "shh"}

result = {}

for key in dict1:
    if key in dict2:
        result[key] = dict1[key] + " & " + dict2[key]   # combine values
    else:
        result[key] = dict1[key]

for key in dict2:
    if key not in result:
        result[key] = dict2[key]

print(result)
