# Library management app

class Book:
    def __init__(self, title="", current_borrowers=[], copies=0):

        self.title = title
        self.current_borrowers = current_borrowers
        self.copies = copies

    def __str__(self):
        return f"{self.title}, {self.current_borrowers}, {self.copies}"
    

class User:

    def __init__(self, name, borrowed_books = Book, fines = 0):
        self.name = name 
        self.borrowed_books = borrowed_books
        self.fines = fines

    def __str__(self):
        return f"{self.name}, {self.borrowed_books}, {self.fines}"


class Library:
    def __init__(self, books: list[Book]):
        self.books = books

    def checkout_book(self, book_title: str, user: User):
        if isinstance(book_title, str) == False:
            raise TypeError("Book title must be a string")
               
        for book in self.books:
            if book_title == book.title:
                if book.copies > 0 and len(user.borrowed_books) < 3:
                    book.copies -= 1
                    book.current_borrowers.append(user)
                    user.borrowed_books.append(book)
                    
                else: 
                    print("The book is unavailable or the user has too many books borrowed")
            else:
                print("There is no such a book in the Library")
    
    def return_book(self, book_title:str, user:User):
        
        fine_ind = int(input("Is this a late return please input '1' if yes and '0' if the book is returned in time: "))
      #  if fine_ind == 1:

                
        if book_title in user.borrowed_books:
            book_title.copies += 1
            user.borrowed_books.remove(book_title)
            book_title.current_borrowers.remove(user)
            if fine_ind == 0:
                user.fines = 0
            else:
                user.fines +=1
        else:
            print("There is no such a title borrowed.")

# Creating Users and Books 
User = ["John", "Ben", "Bill", "Glen", " Sophie", "Adam"]
Book = ["Spelling Book", "History", "Geomaps", "Japan stories"]
print(User)
print (Book)

print("Welcome to the Library! Would you like to borrow a book?")