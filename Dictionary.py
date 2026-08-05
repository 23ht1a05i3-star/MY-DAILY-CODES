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