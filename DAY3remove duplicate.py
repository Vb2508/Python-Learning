list1= [1,2,3,6,6,8,10,10,1]
New_List = []
for item in list1:
    if item not in New_List:
        New_List.append(item)
print(New_List)

# list = [1,2,3,4,5,6,7,8]
# list2 =[]
# for i in list:
#     if i%2 ==0:
#         list2.append(i)
# print(list2)