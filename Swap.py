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