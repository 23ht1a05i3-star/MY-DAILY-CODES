#An array is a collection of elements of the same data type stored in a single variable.


# | Method   | Description                               |
# | ---------| ----------------------------------------- |
# | array()  | Creates an array                          |
# | append() | Adds an element at the end                |
# | insert() | Inserts an element at a specific position |
# | remove() | Removes an element by value               |
# | pop()    | Removes an element by index               |
# | index()  | Returns the index of an element           |
# | len()    | Returns the number of elements            |
# | sum()    | Returns the sum of elements               |
# | max()    | Returns the largest element               |
# | min()    | Returns the smallest element              |



#             DIFFERENCE BETWEEN LIST AND ARRAY IN PYTHON


# Definition
# ----------
# List:
# A list is a built-in Python data structure used to store multiple items.
# It can store elements of different data types.

# Array:
# An array is a data structure used to store elements of the same data type.
# In Python, arrays are created using the 'array' module or NumPy.



# Feature                List                          Array

# Module Required        No                            Yes (array or NumPy)

# Data Types             Different data types          Same data type only

# Memory Usage           More memory                   Less memory

# Performance            Slower for numerical data     Faster for numerical data

# Flexibility            Highly flexible               Less flexible

# Built-in Support       Built into Python             Requires importing a module

# Operations             General-purpose               Numerical calculations

# Syntax                 []                            array.array()


# Example of List

# numbers = [10, 20, 30, 40]
# data = [10, "Python", 3.14, True]

# Example of Array

# numbers = array('i', [10, 20, 30, 40])


# Advantages of List

# 1. Built into Python.
# 2. Stores different data types.
# 3. Easy to create and modify.
# 4. Many built-in methods.
# 5. Best for general programming.

# Advantages of Array
# 1. Uses less memory.
# 2. Faster for numerical operations.
# 3. Stores only one data type.
# 4. Suitable for mathematical calculations.
# 5. Better performance for large datasets.
#printing the elements in array
numbers = [10, 20, 30, 40, 50]
for num in numbers:
    print(num)

#accessing the elements in array
numbers =  [10, 20, 30, 40]
#using there index values
print(numbers[0])
print(numbers[2])

#updating the values in array using the index values
numbers = [10, 20, 30]
numbers[1] = 50
print(numbers)

#append the values at the end using append()
numbers = [10, 20, 30]
numbers.append(40)
print(numbers)

#inserting the value and over requirement place we can add
numbers = [10, 20, 40]
#we cangive the position where we want to add
numbers.insert(2, 30)
print(numbers)

#remove the arrayvalue
numbers = [10, 20, 30, 40]
numbers.remove(30)
print(numbers)

#deleting the element using pop
numbers = [10, 20, 30, 40]
numbers.pop(1)
print(numbers)

#searching an element in array
numbers = [10, 20, 30, 40]
search = int(input("Enter number: "))
if search in numbers:
    print("Element Found")
else:
    print("Element Not Found")

#counnting the repetatinn of the element in array
numbers = [10, 20, 10, 30, 10]
print(numbers.count(10))

#reversing the array
numbers = [10, 20, 30, 40]
numbers.reverse()
print(numbers)

#sorting the array
numbers =  [50, 20, 40, 10, 30]
sorted_numbers = sorted(numbers)
print(sorted_numbers)

#Student Marks List
# Store student marks
marks = [75, 82, 90, 68, 88]
print("Student Marks:")
for mark in marks:
    print(mark)
print("Highest Marks:", max(marks))
print("Lowest Marks:", min(marks))
print("Average Marks:", sum(marks) / len(marks))

#Shopping Cart
cart = ["Milk", "Bread", "Rice"]
print("Shopping Cart:", cart)
cart.append("Eggs")
print("After Adding:", cart)
cart.remove("Bread")
print("After Removing:", cart)

#Employee ID Search
employee_ids = [101, 102, 103, 104, 105]
search = int(input("Enter Employee ID: "))
if search in employee_ids:
    print("Employee Found")
else:
    print("Employee Not Found")

#Attendance System
attendance = ["Rahul", "Priya", "Kiran", "Anu"]
print("Present Students:")
for student in attendance:
    print(student)
print("Total Students Present:", len(attendance))

#Bus Seat Booking
seats = [1, 2, 3, 4, 5]
book = int(input("Enter Seat Number to Book: "))
if book in seats:
    seats.remove(book)
    print("Seat Booked Successfully")
else:
    print("Seat Not Available")

print("Available Seats:", seats)
