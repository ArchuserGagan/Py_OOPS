#aggregation = Represents a relationship where one object (the whole) contains
# reference to one or more independent objects (the parts)


class Library:
    def __init__(self, name) -> None:
        self.name = name
        self.books = []

    def add_book(self, book) -> None:
        self.books.append(book)

    def list_books(self) -> list:
        return[f"{book.title} by {book.author}" for book in self.books]
    

class Book:
    def __init__(self, title, author) -> None:
        self.title = title
        self.author = author

library = Library("nyc library")

book1 = Book("psyco", "america")
book2 = Book("pyco", "rica")


library.add_book(book1)
library.add_book(book2)

print(library.name)
for book in library.list_books():
    print(book)
        
        
