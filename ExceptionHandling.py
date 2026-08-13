#Exception handling is a mechanism used to handle runtime errors without stopping
#the entire program suddenly.

a = int(input("Enter number: "))
b = int(input("Enter number: "))
print(a / b)
# try:
#     # risky code

# except:
#     # error handling code

try:
    a = int(input("Enter number: "))
    print(10 / a)
except:
    print("Something went wrong")

#Handling Specific Exceptions
#ZeroDivisionError
try:
    a = int(input("Enter number: "))
    print(100 / a)
except ZeroDivisionError:
    print("Cannot divide by zero")


#ValueError
try:
    age = int(input("Enter age: "))
    print("Age:", age)
except ValueError:
    print("Please enter a number")


#Multiple except

#You can handle different
#  errors separately.
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print(a / b)

except ValueError:
    print("Enter numbers only")
except ZeroDivisionError:
    print("Cannot divide by zero")


#The else block executes
#  only when there is no exception.

try:
    num = int(input("Enter number: "))

except ValueError:
    print("Invalid input")

else:
    print("You entered:", num)

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print("Result:", a / b)

except ValueError:
    print("Enter numbers only")

except ZeroDivisionError:
    print("Cannot divide by zero")

finally:
    print("Program completed")