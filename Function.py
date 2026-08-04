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

#Lambda with Sorting
students = [("Ram", 90), ("Ravi", 75), ("Asha", 95)]
students.sort(key=lambda x: x[1])
print(students)

#Map Function
numbers = [1, 2, 3, 4, 5]
square = list(map(lambda x: x*x, numbers))
print(square)

#Nested Function
def outer():
    print("Outer Function")
    def inner():
        print("Inner Function")
    inner()
outer()

#Calculator using Functions
def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    return a / b
choice = input("Choose (+,-,*,/): ")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if choice == "+":
    print(add(a, b))
elif choice == "-":
    print(sub(a, b))
elif choice == "*":
    print(mul(a, b))
elif choice == "/":
    print(div(a, b))

#Decorator Function (Advanced)
def welcome(func):
    def message():
        print("Welcome")
        func()
        print("Thank You")
    return message
@welcome
def display():
    print("Learning Python Functions")
display()
#. Palindrome Function
def palindrome(text):
    return text == text[::-1]
word = input("Enter a word: ")
if palindrome(word):
    print("Palindrome")
else:
    print("Not Palindrome")

#Armstrong Number Function
def armstrong(num):
    power = len(str(num))
    total = sum(int(d)**power for d in str(num))
    return total == num
n = int(input("Enter number: "))
if armstrong(n):
    print("Armstrong Number")
else:
    print("Not Armstrong")

#Count Vowels using Function
def vowels(text):
    count = 0
    for ch in text.lower():
        if ch in "aeiou":
            count += 1
    return count
name = input("Enter text: ")
print("Vowels =", vowels(name))

#Student Grade Function
def grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 75:
        return "B"
    elif mark >= 50:
        return "C"
    else:
        return "Fail"
marks = int(input("Enter Marks: "))
print("Grade:", grade(marks))

#Count Vowels using Function
def vowels(text):
    count = 0
    for ch in text.lower():
        if ch in "aeiou":
            count += 1

    return count
name = input("Enter text: ")
print("Vowels =", vowels(name))

#Password Validation Function
def check(password):
    if len(password) >= 8:
        print("Strong Password")
    else:
        print("Weak Password")
pwd = input("Enter Password: ")
check(pwd)