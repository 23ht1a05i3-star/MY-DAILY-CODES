# its the latest one finding latest one using three numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
largest = max(a, b, c)
print("Largest Number:", largest)

#Another way finding largest number using two numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if num1 > num2:
    print("Largest number is:", num1)
else:
    print("Largest number is:", num2)

#its modification one of three numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3
print("Largest number is:", largest)

#using map function and finding largest number in list
numbers = [10, 25, 7, 89, 45]
largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
print("Largest number is:", largest)

#Using Nested if
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a > b:
    if a > c:
        print("Largest number is:", a)
    else:
        print("Largest number is:", c)
else:
    if b > c:
        print("Largest number is:", b)
    else:
        print("Largest number is:", c)
        #Using max() Function
        a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
print("Largest number is:", max(a, b, c))

#Without Using max()
numbers = [45, 89, 12, 67, 100, 34]
largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
print("Largest number is:", largest)

#Smallest of Three Numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
smallest = min(a, b, c)
print("Smallest =", smallest)

#another technique
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a < b:
    if a < c:
        print("Smallest number is:", a)
    else:
        print("Smallest number is:", c)
else:
    if b < c:
        print("Smallest number is:", b)
    else:
        print("Smallest number is:", c)

#in list finding the smallest
numbers = [12, 45, 78, 23, 56]
print("Smallest =", min(numbers))