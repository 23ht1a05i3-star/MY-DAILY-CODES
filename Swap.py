#exchamge the numbers (or) swap the  numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

a, b = b, a

print("After swapping:")
print("a =", a)
print("b =", b)


# Swap two numbers using a temporary variable

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Before swapping:")
print("a =", a)
print("b =", b)

# Swapping
temp = a
a = b
b = temp

print("After swapping:")
print("a =", a)
print("b =", b)

#Swap Two Strings
name1 = input("Enter first name: ")
name2 = input("Enter second name: ")
name1, name2 = name2, name1
print("After Swapping")
print("First Name:", name1)
print("Second Name:", name2)

#Swap Two Characters
ch1 = input("Enter first character: ")
ch2 = input("Enter second character: ")
ch1, ch2 = ch2, ch1
print("After Swapping")
print("Character 1:", ch1)
print("Character 2:", ch2)

#Swap Two Decimal Numbers
a = float(input("Enter first decimal number: "))
b = float(input("Enter second decimal number: "))
a, b = b, a
print("After Swapping")
print("a =", a)
print("b =", b)