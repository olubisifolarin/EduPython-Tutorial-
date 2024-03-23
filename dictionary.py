# DICTIONARY
fruits = {"apple", "mango", "pawpaw", "carrot", "pear"}
print(fruits)

my_dict = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i'}
print(my_dict)

animals = {"dog": "a domestic animal", "cat": "a domestic animal", "fish": "an aquatic animal"}

# SET
my_set = {"apple", "banana", "orange", "pear"}
print(my_set)

animals = {"dog", "cat", "rabbit", "goat"}

# CONVERTING OUR LIST TO SET
my_list = [1, 2, 3, 4, 3, 2, 1]
my_set = set(my_list)
print(my_set) 

# CONVERTING A STRING TO A SET
my_string = "hello"
my_set = set(my_string)
print(my_set)

# ACESSING IN DICTIONARY SET
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
print(my_dict['name'])
print(my_dict.get('age'))
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())

# MODIFYING IN DICTIONARY SET
my_dict['age'] = 40
print(my_dict)

my_dict['name'] = "Byrant"
print(my_dict)

my_dict['country'] = "Nigeria"
print(my_dict)

del my_dict['city']
print(my_dict)

my_dict.clear()
print(my_dict)

# SET METHODS
my_set = {1, 2, 3}
my_set.add(4)
print(my_set)

my_set = {1,2,3,4,5}
my_set.remove(3)
print(my_set)

my_set = {1,2,3,4,5}
my_set.clear()
print(my_set)

my_set = {1, 2, 3}
print(2 in my_set)  
print(4 in my_set)

my_set = {1, 2, 3}
other_set = {3, 4, 5}
my_set.update(other_set)
print(my_set)

my_set = {1, 2, 3}
copy_set = my_set.copy()
print(copy_set) 

file_path = "c:/Users/dell/Desktop/Scopic.docx"

f = open(file_path, "r")
f.close

# f= open("c:/Users/dell/Desktop/Training", "x")

f = open("c:/Users/dell/Desktop/Scopic.docx", "w")
f.write("My name is Folarin")
f.close

import os
file_path = "c:/Users/dell/Desktop/Training"
os.rmdir(file_path)