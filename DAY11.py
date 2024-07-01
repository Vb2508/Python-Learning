class LibraryBook:
    def __init__(self):
        self.listOfBooks=[]
    def addBook (self,book):
        #print(book)
        self.listOfBooks.append(book)

    def remove (self,book):    
      print(book)


    def ShowListOfBooks (self):
        for item in  self.listOfBooks:
            print(item)

        
         



v=  LibraryBook()
v.addBook({"id":1,"book1":"Autobiography of Yogi", "BookBy":"Paramahansa Yogananda"})
v.addBook({"id":2,"book2":"The Power of your subconscious mind", "BookBy":"Joseph Murphy"})
v.addBook({"id":3,"book3":"The Immortals of Meluha", "BookBy":"Amish Tripathi"})
v.ShowListOfBooks()

