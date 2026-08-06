#Bitwise AND (&)
a = 10
b = 6
print("a =", a)
print("b =", b)
print("a & b =", a & b)

#Bitwise OR (|)
a = 10
b = 6
print("a | b =", a | b)

#Bitwise XOR (^)
a = 10
b = 6
print("a ^ b =", a ^ b)

#Bitwise NOT (~)
a = 10
print("~a =", ~a)

#Left Shift (<<)
a = 5
print(a << 1)
print(a << 2)

#Right Shift (>>)
a = 20
print(a >> 1)
print(a >> 2)

#User Input Example
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("AND :", a & b)
print("OR  :", a | b)
print("XOR :", a ^ b)

#Check Even or Odd Using Bitwise
num = int(input("Enter a number: "))
if num & 1:
    print("Odd")
else:
    print("Even")

#Swap Two Numbers Using XOR
a = 15
b = 25

print("Before Swap")
print(a, b)
a = a ^ b
b = a ^ b
a = a ^ b
print("After Swap")
print(a, b)

#Check Power of 2
num = int(input("Enter a number: "))
if num > 0 and (num & (num - 1)) == 0:
    print("Power of 2")
else:
    print("Not a Power of 2")

#Print Binary Representation
num = int(input("Enter a number: "))
print("Binary:", bin(num))

#Mini Bitwise Calculator
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("\nAND :", a & b)
print("OR  :", a | b)
print("XOR :", a ^ b)
print("NOT of a :", ~a)
print("Left Shift :", a << 1)
print("Right Shift:", a >> 1)

#Find Whether a Number is Even or Odd Using Bitwise Operator
num = int(input("Enter a number: "))
if num & 1:
    print(num, "is Odd")
else:
    print(num, "is Even")

#Count the number of set bits in an integer.
num = int(input("Enter a number: "))
count = 0
while num > 0:
    count += num & 1
    num = num >> 1
print("Number of set bits:", count)

#Toggle the 4th bit of a number.
num = int(input("Enter a number: "))

position = 4      
result = num ^ (1 << position)
print("Original Number :", num)
print("Modified Number :", result)