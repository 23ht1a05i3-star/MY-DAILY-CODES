# OOP (Object-Oriented Programming) is one 
# of the most important topics in Python, 
# especially if you want to build real projects.

# The main concepts are:

# Class
# Object
# Constructor
# Instance Variables
# Methods
# Encapsulation
# Inheritance
# Polymorphism
# Abstraction

class Student:
    def display(self):
        print("I am a student")
student1 = Student()
student2 = Student()
student1.display()
student2.display()

#The __init__() method is automatically executed when an object is created.
#Basic program
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
student = Student("Narendra", 21)
print(student.name)
print(student.age)

#Instance
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
student1 = Student("Narendra", 90)
student2 = Student("Dinesh", 85)
print(student1.name)
print(student2.name)

#Instance Methods
#A method is a function defined inside a class.
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)
student = Student("Narendra", 92)
student.display()