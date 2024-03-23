
# READING A FILE
file = open("c:/Users/dell/Desktop/Scopic.docx", "r+")
content = file.read()
file.close()

# WRITING A FILE
file = open("c:/Users/dell/Desktop/Scopic.docx", "w+")
content = file.write("This is Edupassare Python class")
file.close()

# CREATING A FILE
f = open("c:/Users/dell/Desktop/Dog", "x")

#  TO DELETE A FOLDER
import os

os.rmdir("c:/Users/dell/Desktop/Dog")

#  TO DELETE A FILE
import os

os.remove("c:/Users/dell/Desktop/Dog/dog.html")

# HANDLING EXCEPTION

try:
    file = open("c:/Users/dell/Document/Dog", "r")
except FileNotFoundError:
    print("File not found")
    
try:
    file = open("c:Users/dell/Desktop/Dog", "w")
except PermissionError:
    print("Permission Denied")
    
try:
    file = open("c:Users/dell/Desktop/Dog", "w")
except IOError:
    print("Permission Denied")    
    
try: 
    file = open("c:Users/dell/Desktop/Dog", "r")
except ValueError:
    print("Input or Output error")
    
try: 
    file = open("c:Users/dell/Desktop/Dog", "r")
except ModuleNotFoundError:
    print("Input or Output error")
    
try: 
    file = open("c:Users/dell/Desktop/Dog", "r")
except AttributeError:
    print("Input or Output error")
    

    