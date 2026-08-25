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



#     try
#  ↓
# Error?
#  ↙   ↘
# YES   NO
#  ↓     ↓
# except else

#finally
#The finally block executes whether 
# an exception occurs or not
try:
    num = int(input("Enter number: "))
    print(10 / num)
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("Program completed")
#Complete Exception Handling Structure
# try:
#     # risky code

# except ValueError:
#     # handle ValueError

# except ZeroDivisionError:
#     # handle ZeroDivisionError

# else:
#     # executes if no error

# finally:
#     # always executes

#Calculator with Exception Handling
try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    op = input("Enter operator: ")

    if op == "+":
        print(a + b)

    elif op == "-":
        print(a - b)

    elif op == "*":
        print(a * b)

    elif op == "/":
        print(a / b)

    else:
        print("Invalid operator")

except ValueError:
    print("Enter numbers only")

except ZeroDivisionError:
    print("Cannot divide by zero")

#Student Marks
try:
    marks = int(input("Enter marks: "))
    if marks < 0 or marks > 100:
        print("Invalid marks")
    elif marks >= 40:
        print("Pass")
    else:
        print("Fail")
except ValueError:
    print("Enter numbers only")

#Age Validation
try:
    age = int(input("Enter age: "))

    if age < 0:
        print("Invalid age")

    elif age >= 18:
        print("Eligible")

    else:
        print("Not Eligible")

except ValueError:
    print("Enter a valid age")

#Login System
try:
    username = input("Username: ")
    password = input("Password: ")

    if username == "admin" and password == "1234":
        print("Login Successful")
    else:
        print("Invalid Login")

except Exception as e:
    print("Error:", e)

#File Handling + Exception Handling
try:
    file = open("data.txt", "r")
    print(file.read())
    file.close()
except FileNotFoundError:
    print("File does not exist")

#Bank Account Example
class InsufficientBalance(Exception):
    pass


balance = 5000

try:
    amount = int(input("Enter amount: "))

    if amount > balance:
        raise InsufficientBalance("Not enough balance")

    balance -= amount

    print("Withdrawal Successful")
    print("Balance:", balance)

except InsufficientBalance as e:
    print(e)

except ValueError:
    print("Enter a valid amount")

    print("my exception files")