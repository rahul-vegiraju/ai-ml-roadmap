class Book():
    def __init__(self, title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages

    def read(self):
        return f'{self.author} is reading book with {self.title} as title which has {self.pages} pages.'
    
book1 = Book("Chapter One", "John", "200")
book2 = Book("Chapter 3", "Mary", "30")
book3 = Book("Chapter 15", "Robert", "3000")
print(book1.title)
print(book1.author)
print(book1.pages)
print(book1.read())

print(book2.title)
print(book2.author)
print(book2.pages)

print(book3.read())




