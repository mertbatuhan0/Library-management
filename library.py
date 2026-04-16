class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.employees = []

    def add_book(self, book):
        self.books.append(book)