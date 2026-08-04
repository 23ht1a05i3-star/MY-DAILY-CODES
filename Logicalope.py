#in this we has logical operations and there truth tables
#in this the two values must be true thanit shows true value else it show false
#AND
age = int(input("Enter your age: "))
has_id = input("Do you have an ID? (yes/no): ")

if age >= 18 and has_id == "yes":
    print("You are allowed to vote.")
else:
    print("You are not allowed to vote.")

# Truth Table
# A	     B	    A and B
# 1	      1	    1
# 1       0	    0
# 0       1	    0
# 0       0	    0

#OR
#in it  shows true any one value can true else it have  show false only when two are false
day = input("Enter the day: ")

if day == "Saturday" or day == "Sunday":
    print("It's a holiday!")
else:
    print("It's a working day.")

# Truth Table
# A	B	A or B
# 1	1	1
# 1	0	1
# 0	1	1
# 0	0	0

#Logical NOT
is_raining = False

if not is_raining:
    print("You can go outside.")
else:
    print("Take an umbrella.")


# Truth Table
# A	not A
# 1	0
# 0	1
#ATM Cash Withdrawal (and)
balance = int(input("Enter your account balance: "))
pin = input("Enter your ATM PIN: ")

if balance >= 1000 and pin == "1234":
    print("Withdrawal Successful")
else:
    print("Transaction Failed")

#Free Delivery (or)
amount = float(input("Enter order amount: "))
premium = input("Are you a Premium Member? (yes/no): ")

if amount >= 500 or premium == "yes":
    print("Free Delivery")
else:
    print("Delivery Charges Apply")

#Low Battery Warning (not)
charging = input("Is the phone charging? (yes/no): ")

if not (charging == "yes"):
    print("Please connect your charger.")
else:
    print("Phone is charging.")


#Real world scenarious problem
#Movie Ticket
age = int(input("Enter your age: "))
has_ticket = input("Do you have a ticket? (yes/no): ")
if age >= 18 and has_ticket == "yes":
    print("You can watch the movie.")
else:
    print("Entry Denied.")

#Student Pass (or)
marks = int(input("Enter marks: "))
sports = input("Sports Certificate? (yes/no): ")
if marks >= 35 or sports == "yes":
    print("Student Passed")
else:
    print("Student Failed")

#Door Lock (not)
door_locked = False
if not door_locked:
    print("Please lock the door.")
else:
    print("Door is secure.")

#Internet Connection (not)
connected = input("Is Wi-Fi connected? (yes/no): ")
if not (connected == "yes"):
    print("Connect to Wi-Fi.")
else:
    print("Internet is available.")

#A software company is developing a Decision-Making System to automate different real-life situations using Python logical operators.
#  The system should perform various checks such as voting eligibility, ATM withdrawal, login verification, 
# driving license approval, scholarship eligibility, holiday detection, free delivery, restaurant discounts,
#  library access, school holidays, rain alerts, phone charging reminders, door lock status, Wi-Fi connectivity, battery charging status,
#  college admissions, office entry, online shopping offers, flight boarding, and smart home security
# ===========================================
# PYTHON LOGICAL OPERATORS (AND, OR, NOT)
# Combined Practice Program
# ===========================================

print("=== AND ===")

age = int(input("Age: "))
id = input("ID (yes/no): ")

if age >= 18 and id == "yes":
    print("Eligible to Vote")
else:
    print("Not Eligible")

print("\n=== OR ===")

amount = int(input("Order Amount: "))
member = input("Premium Member (yes/no): ")

if amount >= 500 or member == "yes":
    print("Free Delivery")
else:
    print("Delivery Charges")

print("\n=== NOT ===")

charging = input("Phone Charging (yes/no): ")

if not (charging == "yes"):
    print("Connect Charger")
else:
    print("Charging")

print("\n=== COMBINED ===")

marks = int(input("Marks: "))
sports = input("Sports Certificate (yes/no): ")
fees = input("Fees Paid (yes/no): ")

if (marks >= 75 or sports == "yes") and fees == "yes":
    print("Admission Confirmed")
else:
    print("Admission Pending")