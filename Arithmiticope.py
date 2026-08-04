#addition
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Sum =", a + b)

#subtraction
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Difference =", a - b)

#Multiplication
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Product =", a * b)

#Division
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Quotient =", a / b)



#print multiplication table and i use f string for printing the table
num = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

#Supermarket Billing System
# User Inputs
price = float(input("Enter price of one item: ₹"))
quantity = int(input("Enter quantity: "))
discount = float(input("Enter discount amount: ₹"))
people = int(input("Enter number of people sharing the bill: "))

# Multiplication (*)
total_cost = price * quantity
print("Total Cost = ", total_cost)

# Subtraction (-)
final_bill = total_cost - discount
print("Bill After Discount = ", final_bill)

# Division (/)
bill_per_person = final_bill / people
print("Bill Per Person = ", bill_per_person)

# Floor Division (//)
whole_amount = final_bill // people
print("Whole Amount Per Person = ", whole_amount)

# Modulus (%)
remaining = final_bill % people
print("Remaining Amount = ", remaining)

# Exponent (**)
reward_points = quantity ** 2
print("Reward Points Earned =", reward_points)

# Addition (+)
wallet_balance = 500
updated_balance = wallet_balance + 100
print("Wallet Balance After Cashback = ", updated_balance)