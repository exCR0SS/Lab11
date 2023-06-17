hashmap = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten"}

keys = []
for key in hashmap:
    if key > 5:
        keys.append(key)

if 0 in keys:
    values = []
    for key in hashmap:
        if key == 0:
            values.append(hashmap[key])
    print(", ".join(values))
else:
    product = 1
    for key in hashmap:
        if len(hashmap[key]) > 5:
            product *= key
    print(product)