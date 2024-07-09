class Cricket:


    def __init__(self):
        self.Cricket_Kit=[]

    def  add_bat(self,sg):
        self.Cricket_Kit.append(sg)
        return self.Cricket_Kit
    
    def remove_bat(self,name):
        for index, item in enumerate(self.Cricket_Kit):
            if name==item["name"]:
             item =self.Cricket_Kit.pop(index)
             return index,item,"removed"
                


main=Cricket()
a=main.add_bat({"name":"sunny","type":"English willow"})
a=main.add_bat({"name":"Xtreme","type":"Kashmir willow"})
print(a)
b=main.remove_bat("Xtreme")
print(b)


# def add(a,b):
#     c = a+b
#     return c
# #     print(c)
# result = add(10,20)
# # print(result)


# class add:
#     def __init__(self,add):
#         self.add=add

#     def add1(self,a,b):
#         c= a+b
#         # print(a+b)
#         return c
    
    
# v= add(1,2)
# print(v)
    




