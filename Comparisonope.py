#Equall(==)
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print(a == b)
#in this we get output as true (or) false

#Not Equall(!=)
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print(a != b)

#greater than(>)
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print(a > b)

#Less than(<)
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print(a < b)

#Greater than or  equall to(>=)
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print(a >= b)

#Less thanor equall to(<=)
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print(a <= b)

#by this operations there willbe output generated in boolean valkues only 
#bollean values means true or false only



#exampleson real world cenarious 
#ATM Minimum Balance Check
balance = int(input("Enter your account balance: "))

if balance >= 1000:
    print("You can withdraw money.")
else:
    print("Minimum balance not maintained.")


#Movie Ticket Eligibility

age = int(input("Enter your age: "))

if age >= 18:
    print("You can watch the movie.")
else:
    print("Parental guidance required.")


#Passwoard Verification
password = input("Enter Password: ")

if password == "python123":
    print("Login Successful.")
else:
    print("Incorrect Password.")

#Checking if pin is correct or not
correct_pin = "1234"

entered_pin = input("Enter your ATM PIN: ")

if entered_pin != correct_pin:
    print("Incorrect PIN. Access Denied.")
else:
    print("PIN Verified. Welcome!")