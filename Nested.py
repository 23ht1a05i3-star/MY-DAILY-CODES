# A nested condition means writing one if statement inside another if statement.

# It is useful when the second condition should be checked only 
# after the first condition is true.


#Basic condition to work on nested conditions
# if condition1:
#     if condition2:
#         print("Both conditions are true")
#     else:
#         print("Second condition is false")
# else:
#     print("First condition is false")

age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Entry Allowed")
    else:
        print("ID Required")
else:
    print("Under Age")


#Student Exam Eligibility
marks = int(input("Enter marks: "))

if marks >= 40:
    attendance = int(input("Enter attendance: "))

    if attendance >= 75:
        print("Eligible for Exam")
    else:
        print("Attendance is low")
else:
    print("Marks are too low")

#Login System
username = input("Username: ")

if username == "admin":
    password = input("Password: ")

    if password == "1234":
        print("Login Successful")
    else:
        print("Wrong Password")
else:
    print("Wrong Username")

#ATM Withdrawal
balance = 10000
pin = input("Enter PIN: ")

if pin == "1234":
    amount = int(input("Enter amount: "))

    if amount <= balance:
        print("Withdrawal Successful")
        print("Balance:", balance - amount)
    else:
        print("Insufficient Balance")
else:
    print("Invalid PIN")

#