class Contact:
    def __init__(self):
        self.ContatctList=[]
        self.id = 1
        self.location = "blr"
    def addcontact(self,contact):
        
        # print(contact,"added successfully")
        contact.update({"id":self.id,"location":"blr"})
        self.id = self.id + 1
        self.location= self.location
        

        
        self.ContatctList.append(contact)
        print(contact)



    def showcontactlist(self):
        for item in self.ContatctList:
            print(item)
        print(self.ContatctList,"final list")


    def removeContact(self,id):
        for index,item in enumerate(self.ContatctList):
            if id == item ["id"]:
             self.ContatctList.pop(index)
             print(item,"removed contact")

    def replaceContact(self,id,key, value):
        for item in self.ContatctList:
            if id==item["id"]:
             print(item)
            item.update({key:value})
            print(item,"updated id")
B=Contact()
B.addcontact({"ContactName":"vivek b","ContactNumber":"9049391822"})
B.addcontact({"ContactName":"vivek b1","ContactNumber":"8237253494"})
B.addcontact({"ContactName":"Malak","ContactNumber":"9518937690"})
B.replaceContact(2,"ContactName","vivek b01")
B.removeContact(1)