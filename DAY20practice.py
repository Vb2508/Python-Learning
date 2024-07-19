
list= ["a","b","c","c","a","d","c"]
count_dict = {}

# Loop to count each character's occurrences
for item in list:
    if item in count_dict:
        count_dict[item] += 1
    else:
        count_dict[item] = 1
print(count_dict)
# Initialize an empty list to maintain the order of first appearances
order = []

# Loop to keep track of the order of first appearances
for item in list:
    if item not in order:
        order.append(item)
# print(order)
# Construct the result string using the order and counts
result = ''.join(f"{count_dict[char]}{char}" for char in order)
print(result)