b = 20
print("sum of two numbers:",+sum)

name = "Narendra"
age = 21
#mystring and integer
name = "Dinesh"
age = 19

print(name)
print(age)#Decision making ability
#Control flow decides
#1.how many times to execute what to execute

#human analogy:

'''
if it rains --> take the umbrella
if marks > --> pass
if password is correct --> login

'''

#program also needs decisions making ability
#control flow: determines
#which statement to execute and in what order

'''
3-Types of control flow
1.Sequential : Top to bottom execution
2.conditional: decisions making
3.Looping: Repetition

'''
#if --> to check the condition
#& executes if condition is true
#Syntax:
#if condition:
#   statements

#Exampke:
age = 21
if age > 20:
    print("Eligible")

'''
Execution flow
        condition true?
                |
        Execute the block
        
'''

x = 10

if x>5:
    print("Hello")

#if-else :what if state becomes false

#if condition:
#    statement
#else:
#    statements

# Example:    Even/odd

#take input
num = int(input("Enter the number"))

#check the condition
if num% 2 == 0: 
    print("Even number")
else:
    print("Odd numbers")
    
'''
Execution flow
                                                condition
                                                /    \
                                             True    False
                                              |       |
                                              Even   Odd
'''

# elif ladder
#Multiple conditions: multiple decisions

#if condition:
#   statement-1
#elif condition-2:
#     statements
# else:
#     statements

#Task: build a stundent grading system

#dont do these mistakes
marks = 90

if marks >= 50:
    print("c")
elif marks >=90:
    print("A")
else:
    print("Fail")

#Positive, Negative or Zero
num = int(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

#Age Category
age = int(input("Enter your age: "))
if age < 13:
    print("Child")
elif age < 20:
    print("Teenager")
elif age < 60:
    print("Adult")
else:
    print("Senior Citizen")

#Largest of Two Numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a > b:
    print("First number is largest")
elif b > a:
    print("Second number is largest")
else:
    print("Both are equal")

#Electricity Bill
units = int(input("Enter units: "))
if units <= 100:
    bill = units * 2
elif units <= 200:
    bill = units * 3
else:
    bill = units * 5
print("Bill =", bill)

#Simple Calculator
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter +, -, *, /: ")
if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    if b != 0:
        print(a / b)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid operator")

#ATM Withdrawal
balance = int(input("Enter balance: "))
amount = int(input("Enter withdrawal amount: "))
if amount <= 0:
    print("Invalid amount")
elif amount > balance:
    print("Insufficient balance")
elif amount % 100 != 0:
    print("Enter amount in multiples of 100")
else:
    balance -= amount
    print("Withdrawal Successful")
    print("Remaining Balance:", balance)

#Student Result System
marks = int(input("Enter marks: "))
if marks < 0 or marks > 100:
    print("Invalid marks")
elif marks >= 90:
    print("A Grade - Excellent")
elif marks >= 75:
    print("B Grade - Very Good")
elif marks >= 60:
    print("C Grade - Good")
elif marks >= 40:
    print("D Grade - Pass")
else:
    print("F Grade - Fail")

#Temperature Checker
temp = float(input("Enter temperature: "))

if temp >= 40:
    print("Very Hot")
elif temp >= 30:
    print("Hot")
elif temp >= 20:
    print("Normal")
elif temp >= 10:
    print("Cold")
else:
    print("Very Cold")

#Student Scholarship
marks = int(input("Enter marks: "))
attendance = int(input("Enter attendance: "))
if marks >= 90 and attendance >= 90:
    print("100% Scholarship")
elif marks >= 80 and attendance >= 85:
    print("50% Scholarship")
elif marks >= 70 and attendance >= 80:
    print("25% Scholarship")
else:
    print("No Scholarship")

#Employee Bonus
salary = float(input("Enter salary: "))
years = int(input("Enter years of experience: "))
if years >= 10:
    bonus = salary * 0.20
elif years >= 5:
    bonus = salary * 0.10
elif years >= 2:
    bonus = salary * 0.05
else:
    bonus = 0
print("Bonus:", bonus)
print("Total Salary:", salary + bonus)

#ATM with Multiple Conditions
balance = 10000
pin = input("Enter PIN: ")
amount = int(input("Enter amount: "))
if pin != "1234":
    print("Wrong PIN")
elif amount <= 0:
    print("Invalid amount")
elif amount > balance:
    print("Insufficient Balance")
elif amount % 100 != 0:
    print("Amount must be multiple of 100")
else:
    balance -= amount
    print("Transaction Successful")
    print("Balance:", balance)