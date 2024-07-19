# weight = input("total weight avg:").split()
# sum=0
# count =0

# for i in weight:
#     sum= int(sum)+int(i)
# print (sum)

# for item in weight:
#     count=count+1
# print(count)    


# avg_of_total_weight=sum/count
# print(avg_of_total_weight)


numbers = [3, 5, 2, 8, 1, 10]

# Check if the list is empty
for item in not numbers:
    if item !=numbers:
        max_number = None  # Set max_number to None if the list is empty
else:
    max_number = numbers[0]  # Assume the first number is the maximum

    # Iterate through the list
    for number in numbers:
        if number > max_number:
            max_number = number  # Update max_number if the current number is greater

# Print the maximum number
print(f"The maximum number in the list is: {max_number}")