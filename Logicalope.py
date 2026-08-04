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

print("========== AND OPERATOR ==========")

# 1. Voting Eligibility
age = int(input("Enter your age: "))
has_id = input("Do you have an ID? (yes/no): ")

if age >= 18 and has_id == "yes":
    print(" You are allowed to vote.")
else:
    print(" You are not allowed to vote.")

print("----------------------------------")

# 2. ATM Withdrawal
balance = int(input("Enter your account balance: "))
pin = input("Enter your ATM PIN: ")

if balance >= 1000 and pin == "1234":
    print(" Withdrawal Successful")
else:
    print(" Transaction Failed")

print("----------------------------------")

# 3. Login System
username = input("Enter Username: ")
password = input("Enter Password: ")

if username == "admin" and password == "python123":
    print(" Login Successful")
else:
    print(" Invalid Username or Password")

print("----------------------------------")

# 4. Driving License
age = int(input("Enter your age: "))
test = input("Did you pass the driving test? (yes/no): ")

if age >= 18 and test == "yes":
    print(" License Approved")
else:
    print(" License Rejected")

print("----------------------------------")

# 5. Scholarship
marks = int(input("Enter your marks: "))
attendance = int(input("Enter attendance percentage: "))

if marks >= 75 and attendance >= 80:
    print(" Scholarship Approved")
else:
    print(" Scholarship Not Approved")



print("\n========== OR OPERATOR ==========")

# 6. Holiday
day = input("Enter the day: ")

if day == "Saturday" or day == "Sunday":
    print(" It's a Holiday")
else:
    print(" It's a Working Day")

print("----------------------------------")

# 7. Free Delivery
amount = float(input("Enter order amount: "))
premium = input("Are you a Premium Member? (yes/no): ")

if amount >= 500 or premium == "yes":
    print(" Free Delivery")
else:
    print(" Delivery Charges Apply")

print("----------------------------------")

# 8. Restaurant Discount
bill = float(input("Enter bill amount: "))
member = input("Are you a Member? (yes/no): ")

if bill >= 1000 or member == "yes":
    print(" Discount Applied")
else:
    print(" No Discount")

print("----------------------------------")

# 9. Library Access
student = input("Are you a Student? (yes/no): ")
teacher = input("Are you a Teacher? (yes/no): ")

if student == "yes" or teacher == "yes":
    print(" Library Access Granted")
else:
    print(" Access Denied")

print("----------------------------------")

# 10. School Holiday
festival = input("Is today a Festival? (yes/no): ")
sunday = input("Is today Sunday? (yes/no): ")

if festival == "yes" or sunday == "yes":
    print(" School Holiday")
else:
    print(" School Open")



print("\n========== NOT OPERATOR ==========")

# 11. Rain Check
is_raining = False

if not is_raining:
    print(" You can go outside.")
else:
    print(" Take an umbrella.")

print("----------------------------------")

# 12. Phone Charging
charging = input("Is the phone charging? (yes/no): ")

if not (charging == "yes"):
    print(" Please connect your charger.")
else:
    print(" Phone is charging.")

print("----------------------------------")

# 13. Door Lock
door_locked = False

if not door_locked:
    print(" Please lock the door.")
else:
    print(" Door is secure.")

print("----------------------------------")

# 14. Wi-Fi Connection
connected = input("Is Wi-Fi connected? (yes/no): ")

if not (connected == "yes"):
    print(" Connect to Wi-Fi.")
else:
    print(" Internet is available.")

print("----------------------------------")

# 15. Battery Status
battery_full = input("Is battery full? (yes/no): ")

if not (battery_full == "yes"):
    print(" Keep Charging.")
else:
    print(" Charging Complete.")



print("\n========== COMBINED (AND + OR + NOT) ==========")

# 16. College Admission
marks = int(input("Enter Marks: "))
sports = input("Sports Certificate? (yes/no): ")
fees = input("Fees Paid? (yes/no): ")

if (marks >= 75 or sports == "yes") and not (fees == "no"):
    print(" Admission Confirmed")
else:
    print(" Admission Pending")

print("----------------------------------")

# 17. Office Entry
id_card = input("Do you have ID Card? (yes/no): ")
fingerprint = input("Fingerprint Verified? (yes/no): ")
blacklisted = input("Are you Blacklisted? (yes/no): ")

if id_card == "yes" and fingerprint == "yes" and not (blacklisted == "yes"):
    print(" Office Entry Allowed")
else:
    print(" Office Entry Denied")

print("----------------------------------")

# 18. Online Shopping Offer
amount = float(input("Enter Shopping Amount: "))
coupon = input("Do you have Coupon? (yes/no): ")
premium = input("Premium Member? (yes/no): ")

if (amount >= 1000 and coupon == "yes") or premium == "yes":
    print(" Offer Applied")
else:
    print(" No Offer")

print("----------------------------------")

# 19. Flight Boarding
ticket = input("Do you have Ticket? (yes/no): ")
passport = input("Do you have Passport? (yes/no): ")
banned = input("Are you Banned? (yes/no): ")

if ticket == "yes" and passport == "yes" and not (banned == "yes"):
    print(" Boarding Allowed")
else:
    print(" Boarding Denied")

print("----------------------------------")

# 20. Smart Home Security
door = input("Is the door closed? (yes/no): ")
window = input("Are the windows closed? (yes/no): ")
fire = input("Is there a fire? (yes/no): ")

if door == "yes" and window == "yes" and not (fire == "yes"):
    print(" Home is Safe")
else:
    print(" Security Alert!")

print("\n========== PROGRAM COMPLETED ==========")