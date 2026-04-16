class Person:
    def __init__(self, name, id):
        self.name = name
        self.id = id

class User(Person):
    def __init__(self, name, id):
        super().__init__(name, id)
        self.borrowed_books = []

class Employee(Person):
    def __init__(self, name, id, position):
        super().__init__(name, id)
        self.position = position


