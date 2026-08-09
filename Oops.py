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

#Encapsulation-->used for encapsulation and for security

#Encapsulation means combining data and methods 
# inside a class and controlling access to internal data.
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
    def show_balance(self):
        print("Balance:", self.__balance)
account = BankAccount(5000)
account.deposit(2000)
account.show_balance()

#Inheritance
#Inheritance allows one class
#  to acquire properties and methods from another class.

class Animal:
    def eat(self):
        print("Animal is eating")
class Dog(Animal):
    def bark(self):
        print("Dog is barking")
dog = Dog()
dog.eat()
dog.bark()

#Types of Inheritance

# Python supports:

# Single Inheritance
# Multiple Inheritance
# Multilevel Inheritance
# Hierarchical Inheritance
# Hybrid Inheritance

# Single Inheritance
class Animal:
    def eat(self):
        print("Eating")
class Dog(Animal):
    def bark(self):
        print("Barking")
dog = Dog()
dog.eat()
dog.bark()

#Multilevel Inheritance
class GrandParent:
    def house(self):
        print("Grandparent's house")
class Parent(GrandParent):
    def car(self):
        print("Parent's car")
class Child(Parent):
    def bike(self):
        print("Child's bike")
child = Child()
child.house()
child.car()
child.bike()