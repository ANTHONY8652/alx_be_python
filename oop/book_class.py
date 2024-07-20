class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        print("Deleting " + self.title)

    def __str__(self):
        return self.title + " by " + self.author + " published in " + str(self.year )
    
    def __repr__(self):
        return "Book('" + self.title + "', '" + self.author + "', '" + str(self.year) + ")"
    
book = Book("1984", "George Orwell", 1946)
print(str(book))
print(repr(book))
del book