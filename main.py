from author import Author
from book import Book
from person import User, Employee
from library import Library


my_library = Library("Biblioteka Uniwersetycka")

writer = Author("J.K. Rowling")
book1= Book(writer, "Harry Potter")

my_library.add_book(book1)
print(f"library: {my_library.name}")
print(f"added book:  {book1}")

e1 = Employee("batuhan", 1, "Library Worker")
u1= User("mert", 36180)

print(f"employee: {e1.name}, duty: {e1.position}")
print(f"user: {u1.name}, ID: {u1.id}")