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

#Percentage Decorator
def result(func):
    def wrapper(mark):
        print("Student Result")
        func(mark)
    return wrapper

@result
def grade(mark):
    if mark >= 35:
        print("Pass")
    else:
        print("Fail")

grade(80)

#. Count Function Calls 
def count_calls(func):
    count = 0
    def wrapper():
        nonlocal count
        count += 1
        print("Function called", count, "times")
        func()
    return wrapper
@count_calls
def hello():
    print("Hello Python")
hello()
hello()
hello()

#Retry on Failure
def retry(func):
    def wrapper():
        for i in range(3):
            try:
                return func()
            except:
                print("Retry", i + 1)
        print("Failed after 3 attempts")
    return wrapper
@retry
def divide():
    a = int(input("Enter Number: "))
    b = int(input("Enter Number: "))
    print(a / b)
divide()

#Login Authentication
def login(func):
    def wrapper():
        username = input("Username: ")
        password = input("Password: ")
        if username == "admin" and password == "python":
            func()
        else:
            print("Access Denied")
    return wrapper
@login
def dashboard():
    print("Welcome Admin")
dashboard()

#Accept Any Number of Arguments
def logger(func):
    def wrapper(*args):
        print("Arguments:", args)
        result = func(*args)
        print("Result:", result)
        return result
    return wrapper
@logger
def add(a, b, c):
    return a + b + c
add(10, 20, 30)

#Multiple Decorators
def upper(func):
    def wrapper():
        return func().upper()
    return wrapper
def star(func):
    def wrapper():
        return "***** " + func() + " *****"
    return wrapper
@star
@upper
def text():
    return "python decorators"
print(text())

#Exception Handling Decorator
def safe(func):
    def wrapper(a, b):
        try:
            return func(a, b)
        except Exception as e:
            print("Error:", e)
    return wrapper
@safe
def divide(a, b):
    return a / b
print(divide(10, 0))