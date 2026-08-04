def decorator(func):
    def wrapper():
        print("Before Function")
        func()
        print("After Function")
    return wrapper
@decorator
def hello():
    print("Hello Python")

hello()
#Welcome Decorator
def welcome(func):
    def message():
        print("Welcome")
        func()
        print("Thank You")
    return message
@welcome
def student():
    print("Learning Python")
student()

#Decorator with Arguments
def decorator(func):
    def wrapper(name):
        print("Welcome")
        func(name)
        print("Visit Again")
    return wrapper
@decorator
def display(name):
    print("Hello", name)
display("Narendra")

#Login Decorator
def login_required(func):
    def wrapper():
        password = input("Enter Password: ")
        if password == "python123":
            func()
        else:
            print("Access Denied")
    return wrapper
@login_required
def profile():
    print("Welcome to Your Profile")
profile()

#Time Decorator
#By using this we have to import the time
import time

def timer(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print("Execution Time:", end - start)
    return wrapper
@timer
def program():
    for i in range(1000000):
        pass
program()

#Uppercase Decorator
def uppercase(func):
    def wrapper():
        return func().upper()
    return wrapper
@uppercase
def message():
    return "welcome to python"
print(message())

#Check Even or Odd using Decorator
def check(func):
    def wrapper(num):
        print("Checking Number...")
        func(num)
    return wrapper
@check
def even(num):
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")
even(8)