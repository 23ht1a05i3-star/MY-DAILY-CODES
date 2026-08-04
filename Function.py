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
add(a,b)
#Subtract Two Numbers using parameters
def subtract(a, b):
    print("Difference =", a - b)
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
subtract(a,b)

#Multiply Two Numbers using parameters
def multiply(a, b):
    print("Product =", a * b)
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
multiply(a,b)

#Divide Two Numbers using parameters
def divide(a, b):
    if b != 0:
        print("Quotient =", a / b)
    else:
        print("Cannot divide by zero")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
divide(a,b)

#Check Even or Odd using function
def check(num):
    if num % 2 == 0:
        print("Even Number")
    else:
        print("Odd Number")
num = int(input("Enter a number: "))
check(num)

#Find Largest Numberusing functions
def largest(a, b):
    if a > b:
        print(a, "is Largest")
    else:
        print(b, "is Largest")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
largest(a, b)

#Prime Number using Function
def prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
n = int(input("Enter a number: "))

if prime(n):
    print("Prime Number")
else:
    print("Not a Prime Number")

#Recursive Factorial
def factorial(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial(n - 1)
num = int(input("Enter number: "))
print("Factorial =", factorial(num))

#Recursive Fibonacci
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
terms = int(input("Enter terms: "))
for i in range(terms):
    print(fibonacci(i), end=" ")