class Contact:
    def __init__(self):
        self.ContatctList=[]

    def addcontact(self,contact):
        # print(contact,"added successfully")
        self.ContatctList.append(contact)
        


    def showcontactlist(self):
        # for item in self.ContatctList:
        #     print(item)
        print("final list",self.ContatctList)


    def removeContact(self,id):
        for index,item in enumerate(self.ContatctList):
            if id == item ["id"]:
             self.ContatctList.pop(index)




B=Contact()
B.addcontact({"id":1,"ContactName":"vivek b","ContactNumber":"9049391822"})
B.addcontact({"id":2,"ContactName":"vivek b1","ContactNumber":"8237253494"})
B.addcontact({"id":3,"ContactName":"Malak","ContactNumber":"9518937690"})

B.removeContact(1)
B.showcontactlist()