# If statement

# x = 25
# if x > 10:
#     print("It is greater")

# a = 8
# if a <= 8:
#     print("a is less than 5")
    
# if Else statement
# age = 21
# if age >= 18:
#     print("You are old")
# else:
#     print("You are young")
    
# if elif else statement

# num = 5
# if num > 0:
#     print("Number is positive")
# elif num < 0:
#     print("Number is negative")
# else:
#     print("Number is zero")
    
# age = 20
# if age > 40:
#     print("You are Old")
# elif age < 40:
#     print("You are Young")
# else:
#     print("You are over aged")

# score = int(input("Enter your score: "))

# if score >= 80:
#     print("Grade A+, You passed the test")
# if score >= 70:
#     print("Grade A, You passed the test")
# elif score >= 60:
#     print("Grade B, You passed the test")
# elif score >= 50:
#     print("Grade C, You passed the test")
# elif score >= 40:
#     print("Grade D, You passed the test")
# else:
#     print("You have failed the test")

    
# # nested if statement
# x = 10
# if x > 5:
#     if x < 15:
#         print("x is between 5 and 15")
        
# number = 30
# if number > 20:
#     if number < 35:
#         print("number is between 20 and 35")
        
# classwork
# Write a program that takes the user's age as input and determines whether they are eligible to vote.

# age = int(input("Enter your age "))

# if age >= 18:
#     print("You are eligible to vote")
# elif age <= 18:
#     print("You are not eligible to vote") 
# else:
#     print("Invalid")   
    
    
# For loop statement
for i in range(5):
    print(i)
    
for num in range(50):
    print(num)

fruits = ["apple", "orange", "pear", "banana", "watermelon"]
for fruit in fruits:
    print(fruit)

# Nested for loop statement
# for i in range(3):
#     for j in range(3):
#         print(i, j)
# CLASS WORK
# Create a for loop that prints the numbers from 1 to 15. 
# for number in range(15):
#     print(number)
    
# While Loop
i = 0
while i < 5:
    print(i)
    i += 1

i = 0
while i < 15:
    print(i)
    i += 1
    
    
num = 10
while num >= 1:
    print(num)
    num -= 1

# NESTED WHILE LOOP
# i = 0
# while i < 3:
#     j = 0
#     while j < 3:
#         print(i, j)
#         j += 1
#     i += 1

# Write a program that takes a user's input for their age and then determines what stage of life they are in (child, teenager, adult, or senior) using if, elif, and else statements.
# age = int(input("Enter your age "))

# age = int(input("Enter your age: "))

# if age < 13:
#     print("You are a child.")
# elif 13 <= age <= 17:
#     print("You are a teenager.")
# elif 18 <= age < 45:
#     print("You are an adult.")
# else:
#     print("You are a senior.")

# Write a program that uses a for loop to print the first 20 even numbers.

# for i in range(2, 20, 2):
#     print(i)

# Write a program that uses a while loop to calculate the sum of all numbers from 1 to 50.
# i = 1
# sum = 0
# while i <= 50:
#     print(i)
#     sum += 1
#     i += 1
    
# tuple_1 = 2, 5, 75, "ola", "seyi"
# tuple_2 = "sam", "dele", "ayo", "kola"
# combined_tuple =(tuple_1 + tuple_2)
# print(combined_tuple)



# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author
#         self.is_borrowed = False

# class Library:
#     def __init__(self):
#         self.books = []

#     def add_book(self, book):
#         self.books.append(book)

#     def display_books(self):
#         for book in self.books:
#             print(f"{book.title} by {book.author}")

#     def borrow_book(self, title):
#         for book in self.books:
#             if book.title == title and not book.is_borrowed:
#                 book.is_borrowed = True
#                 print(f"{title} has been borrowed.")
#                 return
#         print(f"Book {title} not found or already borrowed.")

#     def return_book(self, title):
#         for book in self.books:
#             if book.title == title and book.is_borrowed:
#                 book.is_borrowed = False
#                 print(f"{title} has been returned.")
#                 return
#         print(f"Book {title} not found or not borrowed.")

# # Create some books
# book1 = Book("Things fall apart", "Chinua Achebe")
# book2 = Book("Stay with Me", "Ayọbami Adebayo")
# book3 = Book("Half of a Yellow Sun", "Chimamanda Ngozi Adichie ")

# # Create a library
# library = Library()
# library.add_book(book1)
# library.add_book(book2)
# library.add_book(book3)

# # Display all books in the library
# print("Books available in the library:")
# library.display_books()

# # Borrow a book
# library.borrow_book("Half of a Yellow Sun")
# library.borrow_book("Things Fall Apart")

# # Display all books in the library after borrowing
# print("\nBooks available in the library after borrowing:")
# library.display_books()

# # Return a book
# library.return_book("Stay with Me")

# # Display all books in the library after returning
# print("\nBooks available in the library after returning:")
# library.display_books()
