# # CLASSES AND OBJECT
# class Person:
#     pass

# class Person:
#     def __init__(self, name, age, color, address):
#         self.name = name
#         self.age = age
#         self.color = color
#         self.address = address
        
# my_person = Person("Charles", 12, "Fair", "Lagos")
    
# # class Car:
# #     def __init__(self, brand, model, year):
# #         self.brand = brand
# #         self.model = model
# #         self.year = year
        
# #     def display_info():
# #         pass
    
# # my_car = Car("Toyota", "Camry", 2024)
# # my_car.display_info()

# # class Animal:
# #     def __init__(self, name, color):
# #         self.name = name
# #         self. color = color
# #     print("This is an animal")
    
# #     def walk(self):
# #         print("The dog is walking")
        
# #     def swim(self):
# #         print("The dog is swimming")
    
# # my_animal = Animal("Cat", "White")
# # my_animal.walk()
# # my_animal.swim()


# # INHERITANCE
# # class Person:
# #     def __init__(self, fname, lname):
# #         self.fname = fname
# #         self.lname = lname
        
# #     def  person_data(self):
# #         print(self.fname, self.lname)
        
# #     my_person = Person("Alex", "Byrant")
# #     my_person.person_data()
    
# # class Student(Person):
# #     pass

# # x = Student("Ajiri", "Sultan")
# # x.person_data()


# class Fish:
#    def __init__(self, first_name, last_name="Fish",
#     skeleton="bone", eyelids=False):
#     self.first_name = first_name
#     self.last_name = last_name
#     self.skeleton = skeleton
#     self.eyelids = eyelids

#    def swim(self):
#        print("The fish is swimming.")
       
#    def swim_backwards(self):
#        print("The fish can swim backwards.")

# class Clownfish(Fish):
#     def live(self):
#         print("The clownfish is coexisting with the sea.")
        
        
# class Color:
#     def ___init__(self, green, red, blue, white):
#         self.green = green
#         self.red = red
#         self.blue = blue
#         self.white = white
        
# class ColorPallete(Color):
#     def __init__(self, green, red, blue, white):
#         super().__init__(green, red, blue, white)
#         print("My colors")

# color_pallete = ColorPallete("green", "red", "blue", "white")
# print("These are my favorite colors")

# # POLYMORPHISM
# class Car:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model

#   def move(self):
#     print("Drive!")

# class Boat:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model

#   def move(self):
#     print("Sail!")

# class Plane:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model

#   def move(self):
#     print("Fly!")

# car1 = Car("Ford", "Mustang")       
# boat1 = Boat("Ibiza", "Touring 20")
# plane1 = Plane("Boeing", "747")     


# class Animal:
#     def __init__(self, eyes, nose, leg):
#         self.eyes = eyes
#         self. nose = nose
#         self.leg = leg
    
#     def sound(self):
#         pass 

# class Dog:
#     def __init__(self, eyes, nose, leg):
#         self.eyes = eyes
#         self. nose = nose
#         self.leg = leg
        
#     def sound(self):
#         return "Bark"

# class Goat:
#     def __init__(self, eyes, nose, leg):
#         self.eyes = eyes
#         self. nose = nose
#         self.leg = leg
        
#     def sound(self):
#         return "Bleat"
        
# # a = Animal("two", "one", "four")
# d = Dog("two", "one", "four")
# g = Goat("two", "one", "four")

        
age = 18
if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")

age = 40
if age != 40:
    print("You are Young")
else:
    print("You are Old")

# ASSIGNMENT(Simple Library Management System)
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        for book in self.books:
            print(f"{book.title} by {book.author}")

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title and not book.is_borrowed:
                book.is_borrowed = True
                print(f"{title} has been borrowed.")
                return
        print(f"Book {title} not found or already borrowed.")

    def return_book(self, title):
        for book in self.books:
            if book.title == title and book.is_borrowed:
                book.is_borrowed = False
                print(f"{title} has been returned.")
                return
        print(f"Book {title} not found or not borrowed.")

# Create some books
book1 = Book("Things fall apart", "Chinua Achebe")
book2 = Book("Stay with Me", "Ayọbami Adebayo")
book3 = Book("Half of a Yellow Sun", "Chimamanda Ngozi Adichie ")

# Create a library
library = Library()
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Display all books in the library
print("Books available in the library:")
library.display_books()

# Borrow a book
library.borrow_book("Half of a Yellow Sun")
library.borrow_book("Things Fall Apart")

# Display all books in the library after borrowing
print("\nBooks available in the library after borrowing:")
library.display_books()

# Return a book
library.return_book("Stay with Me")

# Display all books in the library after returning
print("\nBooks available in the library after returning:")
library.display_books()
