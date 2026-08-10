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

#Voting System
age = int(input("Enter age: "))

if age >= 18:
    id_card = input("Do you have ID? yes/no: ")

    if id_card == "yes":
        print("You can vote")
    else:
        print("ID card required")
else:
    print("You are under 18")

#Driving License
age = int(input("Enter age: "))

if age >= 18:
    test = input("Did you pass the test? yes/no: ")

    if test == "yes":
        print("License Approved")
    else:
        print("Test not passed")
else:
    print("Not eligible due to age")

#College Admission
marks = int(input("Enter marks: "))

if marks >= 75:
    entrance = input("Passed entrance exam? yes/no: ")

    if entrance == "yes":
        print("Admission Approved")
    else:
        print("Entrance exam required")
else:
    print("Marks are not sufficient")

#Scholarship System
marks = int(input("Enter marks: "))

if marks >= 80:
    attendance = int(input("Enter attendance: "))

    if attendance >= 85:
        print("Scholarship Approved")
    else:
        print("Attendance too low")
else:
    print("Marks too low")

#Bank Loan Eligibility
salary = int(input("Enter salary: "))

if salary >= 30000:
    credit = int(input("Enter credit score: "))

    if credit >= 700:
        print("Loan Approved")
    else:
        print("Low Credit Score")
else:
    print("Salary not eligible")

#Movie Ticket
age = int(input("Enter age: "))

if age >= 18:
    member = input("Are you a member? yes/no: ")

    if member == "yes":
        print("Ticket Price: ₹150")
    else:
        print("Ticket Price: ₹200")
else:
    print("Ticket Price: ₹100")

#ATM with Multiple Nested Conditions
balance = 10000
pin = input("Enter PIN: ")

if pin == "1234":
    amount = int(input("Enter amount: "))

    if amount > 0:
        if amount <= balance:
            if amount % 100 == 0:
                print("Withdrawal Successful")
                print("Remaining:", balance - amount)
            else:
                print("Enter amount in multiples of 100")
        else:
            print("Insufficient Balance")
    else:
        print("Invalid Amount")
else:
    print("Wrong PIN")