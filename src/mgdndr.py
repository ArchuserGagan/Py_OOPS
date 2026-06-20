#magic method = dunder methods(double underscoe) __init__, __str__, __eq__
# they are automatically called by many of python's built in operations
# they allow developers to define or customize the behaviour


class Book:
    def __init__(self,title,author,num_pages) -> None:
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self) -> str:
        return f"'{self.title}' by {self.author}"
    def __eq__(self, other) -> bool:
        return self.title == other.title and self.author == other.author ## with out eq if two book are identical python will say false
    def __lt__(self, other) -> bool :
        return self.num_pages < other.num_pages
    def __gt__(self, other):
        return self.num_pages > other.num_pages
    def __add__(self, other):
        return f"{self.num_pages + other.num_pages} pages"
    def __contains__(self, keyword):                            #to check keywords 
        return keyword in self.title or keyword in self.author
    def __getitem__(self, key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "num_pages":
            return self.num_pages
        else:
            return f"key '{key}' was not found"
    
    



book1 = Book("subtle art of fuck", "manson", 100)
book2 = Book("every thing is  fucked", "mansn", 100)
book3 = Book("subtle art ", "mason", 100)       

print(book1)
print(book1 == book2)
print(book1 + book3)
print("fuck" in book1)
print(book1['title'])
print(book2['num_pages'])