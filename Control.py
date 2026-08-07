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