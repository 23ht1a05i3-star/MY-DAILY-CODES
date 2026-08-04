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