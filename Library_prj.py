class Library():
    def __init__(self, list):
        self.book_list  = list
        self.book_avail = list[:]
        self.book_rent  = {}

    def availableBook(self):
        for book in self.book_avail:
            print(book)

    def allBook(self):
        for book in self.book_list:
            print(book)

    def rentBook(self, name, book):
        if book not in self.book_list:
            print("The Book is not available.")

        elif book in self.book_avail:
            self.book_rent.update({book: name})
            self.book_avail.remove(book)
            print("The book is available, You Can Take IT.")
            
        else:
             print("The Book is Already Taken by " + self.book_rent[book])
                   

    def returnBook(self, book):
        del self.book_rent[book]
        self.book_avail.append(book)

if __name__ == "__main__":
    obj_lib = Library(["Life of PI", "Merchant of VINECE",
                   "Ulysses", "Jane Eyre","Robinson Crusoe",
                   "The Pilgrim's Progress by John Bunyan"])
    print("------> Welcome To LIBRARY <-------")
    while True:
        print("1. Books in Library")
        print("2. Books Available")
        print("3. Rent Book")
        print("4. Return Book")
        print("5. Quit")
        choice = int(input("Enter Your Choice :"))
        if choice == 1:
            obj_lib.availableBook()
        elif choice == 2:
            obj_lib.allBook()
        elif choice == 3:
            book = input("Enter the Book Name as in LIST : ")
            name = input("Enter Your Name to continue :")
            obj_lib.rentBook(book, name)
        elif choice == 4:
            book = input("Enter the Book Name Going to Return :")
            obj_lib.returnBook(book)
        elif choice == 5:
            print("Invalid Choice")
            break
    
        
        
     
            
            
            
            
