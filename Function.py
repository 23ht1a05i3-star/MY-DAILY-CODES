#A function is a block of code that performs a specific task. 
# It helps avoid writing the same code multiple times.

#creating the  function
def greet():
    print("Welcome to Python")
greet()
#Function with Parameters
#Parameters allow you to pass values to a function.
def add(a, b):
    print("Sum =", a + b)
add(10, 20)
#Function with Return Value
def square(num):
    return num * num
result = square(5)
print(result)

#Lambda Function
#A lambda function is a short anonymous function.
square = lambda x: x * x
print(square(6))

#String Operations
#rings are sequences of characters.
name = "Python"
print(name.upper())
print(name.lower())
print(len(name))
print(name[::-1])

#String Slicing
#its usedfor traversing over the string
text = "Programming"
print(text[0:6])
print(text[3:])
print(text[::-1])

#Add Two Numbers using parameters
def add(a, b):
    print("Sum =", a + b)
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
add(5,6)
#Subtract Two Numbers using parameters
def subtract(a, b):
    print("Difference =", a - b)
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
subtract(4, 5)

#Multiply Two Numbers using parameters
def multiply(a, b):
    print("Product =", a * b)
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
multiply(3,4)

#Divide Two Numbers using parameters
def divide(a, b):
    if b != 0:
        print("Quotient =", a / b)
    else:
        print("Cannot divide by zero")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
divide(3,8)