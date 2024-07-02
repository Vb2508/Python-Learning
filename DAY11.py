# class LibraryBook:
#     def __init__(self):
#         self.listOfBooks=[]
#     def addBook (self,booontatctListk):
#         #print(book)
#         self.listOfBooks.append(book)

#     # def remove (self,book):    
#     #   print(book)

#     def ShowListOfBooks (self):
#         for item in  self.listOfBooks:
#             print(item)

# v=  LibraryBook()
# v.addBook({"id":1,"book1":"Autobiography of Yogi", "BookBy":"Paramahansa Yogananda"})
# v.addBook({"id":2,"book2":"The Power of your subconscious mind", "BookBy":"Joseph Murphy"})
# v.addBook({"id":3,"book3":"The Immortals of Meluha", "BookBy":"Amish Tripathi"})
# v.ShowListOfBooks()



class Contact:
    def __init__(self):
        self.ContatctList=[]

    def addcontact(self,contact):
        # print(contact,"added successfully")
        self.ContatctList.append(contact)
        


    def showcontactlist(self):
        for item in self.ContatctList:
            print(item)

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