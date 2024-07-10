# emp = {"name":"abcd","id":1}
# empList = [{"name":"abcd","id":1},{"name":"xyz","id":2}]
# for item in empList:
#     print('name',item['name'],'id',item['id'])



# def display_emp_list():
#     emp = {"name":"abcd","id":1}
#     empList = [{"name":"abcd","id":1},{"name":"xyz","id":2}]
#     for item in empList:
#         print('name',item['name'],'id',item['id'])
# display_emp_list()




def display_emp_list(marks,x):
   for item in marks:
     result= item*x
     if result %2==0:
        print(result)
     else:
        print("no")

display_emp_list([1,2,3,4],13)
