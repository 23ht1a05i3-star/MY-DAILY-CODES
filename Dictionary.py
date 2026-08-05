# A dictionary is a built-in Python data type used to store data in key-value pairs.

# Keys are unique.
# Values can be duplicated.
# Dictionaries are mutable (can be changed).
# They are written using curly braces {}

#Create a Dictionary
student = {
    "name": "inesh",
    "age": 20,
    "course": "Python"
}
print(student)

#Accessing Values in dictionary
student = {
    "name": "Dinesh",
    "age": 20
}
print(student["name"])
print(student["age"])

#Add a New Item in dictionary
student = {}
student["name"] = "Dinesh"
student["age"] = 20
print(student)

#Update a Value
student = {
    "age": 20
}
student["age"] = 21
print(student)
#Delete an Item
student = {
    "name": "Dinesh",
    "age": 20
}
del student["age"]
print(student)

#Print All Keys
student = {
    "name": "Dinesh",
    "age": 20,
    "course": "Python"
}
for key in student.keys():
    print(key)

#Print Keys and Values
student = {
    "name": "inesh",
    "age": 20,
    "course": "Python"
}

for key, value in student.items():
    print(key, ":", value)

#Real world scenario questions
#Student Management System
students = {}

name = input("Enter Student Name: ")
marks = int(input("Enter Marks: "))
students[name] = marks
print(students)

#ATM Balance Check
accounts = {
    "1001": 5000,
    "1002": 8000
}
acc = input("Enter Account Number: ")
if acc in accounts:
    print("Balance =", accounts[acc])
else:
    print("Account Not Found")

#Shopping Cart
cart = {
    "Rice": 60,
    "Sugar": 45,
    "Oil": 150
}

print("Items:", cart)
item = input("Enter Item: ")
if item in cart:
    print("Price =", cart[item])
else:
    print("Item Not Available")

#Hospital Patient Record
patients = {
    "101": "Fever",
    "102": "Diabetes"
}
pid = input("Patient ID: ")
if pid in patients:
    print("Disease:", patients[pid])
else:
    print("Patient Not Found")

#Country and Capital
country = {
    "India": "New Delhi",
    "Japan": "Tokyo",
    "USA": "Washington D.C."
}
name = input("Country: ")
print(country.get(name, "Country Not Found"))

#Product Price Checker
products = {
    "Laptop": 50000,
    "Mouse": 500,
    "Keyboard": 1000
}
product = input("Product Name: ")
if product in products:
    print("Price =", products[product])
else:
    print("Product Not Found")

#Voting EligibilityVoting Eligibility
voters = {
    "Rahul": 21,
    "Anil": 16
}

name = input("Enter Name: ")

if name in voters:
    if voters[name] >= 18:
        print("Eligible to Vote")
    else:
        print("Not Eligible")
else:
    print("Person Not Found")