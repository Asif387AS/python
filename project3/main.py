class Library:
    def __init__(self,listOfBooks):
        self.books=listOfBooks
    def displayAvailableBooks(self):
        print("The Books present in the libaray:")
        for books in self.books:
            print("*"+books)
    def borrowBook(self,bookName):
        if bookName in self.books:
            print(f"You have been issued {bookName}, Please keep it safe and return it within 30 days")
            self.books.remove(bookName)
            return True
        else:
            print("Sorry! this book is either not availabe or has alread been issued to somebody else.Please wait until the book is availabe")
            return False
    def returnBook(self,bookName):
        self.books.append(bookName)
        print("Thanks for returing this book! Hope you enjoyed reading it .Have a great day ahead!")
class Student:
    def __init__(self):
        self.bookList=[]
    def borrowBook(self):
        self.book=input("Enter the book you want to borrow \n ")
        return self.book
         # self.bookList.append(reqBook)
         
    def returnBook(self):
        self.book=input("Enter the book you want to return \n ")
        return self.book
    


if __name__=="__main__":
    student=Student()
    centralLibrary=Library(["Algorithm","Python","Java","DLD"])
    # centralLibrary.displayAvailableBooks()
    # centralLibrary.borrowBook("Algorithm")
    # centralLibrary.borrowBook("Algorithm")
    # centralLibrary.returnBook("Algorithm")

    while(True):
        welcomeMsg='''====Welcome to Central Library====
        Please Choose an Option
        1.List all the books
        2.Request a book
        3.Add/Return a book
        4.Exit the library'''
        print(welcomeMsg)
        choice=int(input("Enter the choice:"))
        if choice==1:
            centralLibrary.displayAvailableBooks()
        elif choice==2:
            centralLibrary.borrowBook(student.borrowBook())
        elif choice==3:
            centralLibrary.returnBook(student.returnBook())
        elif choice==4:
            print("Thanks for choosing central library! Have a great day ahead")
            exit()
        else:
            print("Invalid choice")
       