# emp = {"name": "vivek",
#        "salary" : "100k"}
# salary = emp ['salary']
# print (salary)


details = {"employeeName" : "Vivek Birajdar",
           "salary"  : "120k",
           "hobbies" : ["Playing cricket","swimming","travelling"],
           "address": {"pincode":1234,"location":"near butst jkgjhik"}}
salary = details["salary"]
hobbies= details["hobbies"]
print(salary, hobbies)
firstHobby = hobbies[0]
print(firstHobby)
name = details["employeeName"]
print(name)
address1 = details["address"]["pincode"]
address2 = details["address"]["location"]
print("my pincode",address1,"my address",address2)