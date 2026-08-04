#A list is a collection of items stored in a single variable.
#in simple worlds list is a group of similler tipes of ellemnts

#basic list
fruits = ["Apple", "Banana", "Mango"]
print(fruits)

#there are some key words in list there are
# 1. append()  -->Adds a new element at the end of the list
# 2. insert()  -->Adds an element at a specific position 
# 3. remove()  -->Removes an element by its value
# 4. pop()  ->Removes and returns an element by its index. If no index is given, it removes the last element
# 5. sort()  -->Sorts the list in ascending order
#6. reverse() -->Reverses the order of the elements
# 7. copy() -->Creates a copy of a list
# 8. count()  -->Counts how many times an element appears
# 9. index()  -->Returns the position (index) of an element
# 10. clear()  -->Removes all elements from the list
# 11. len()  -->Returns the total number of elements in a list
# 12. max()  -->Returns the largest element in the list
# 13. min()   -->Returns the smallest element in the list
# 14. sum()  -->Returns the sum of all numbers in the list
# 15. in()   -->Checks whether an element exists in the list
# 16. not in() -->Checks whether an element does not exist in the list

#1. append()
fruits = ["Apple", "Banana"]
fruits.append("Mango")
print(fruits)

# 2. insert() 
fruits = ["Apple", "Banana"]
fruits.insert(1, "Orange")
print(fruits)

# 3. remove() 
fruits = ["Apple", "Banana", "Mango"]
fruits.remove("Banana")
print(fruits)

# 4. pop()
numbers = [10, 20, 30, 40]
numbers.pop()
print(numbers)

# 5. sort() 
numbers = [50, 10, 30, 20]
numbers.sort()
print(numbers)

#6. reverse()
numbers = [10, 20, 30, 40]
numbers.reverse()
print(numbers)

# 7. copy()
list1 = [10, 20, 30]
list2 = list1.copy()
print(list2)

#8. count()
numbers = [10, 20, 10, 30, 10]
print(numbers.count(10))

#9. index()
fruits = ["Apple", "Banana", "Mango"]
print(fruits.index("Banana"))

#10. clear()
numbers = [10, 20, 30]
numbers.clear()
print(numbers)

#11. len()
students = ["A", "B", "C", "D"]
print(len(students))

#12. max()
numbers = [12, 45, 78, 10]
print(max(numbers))

#13. min()
numbers = [12, 45, 78, 10]
print(min(numbers))

#14. sum()
numbers = [10, 20, 30]
print(sum(numbers))

#15. in
#In this we have only boolesan values
fruits = ["Apple", "Banana", "Mango"]
print("Apple" in fruits)

#16. not in
#Reverseof the in and have generated the boolean values as output
fruits = ["Apple", "Banana", "Mango"]
print("Orange" not in fruits)

# Importance of Lists
# Stores Multiple Values
# Maintains Order
# Dynamic in Size