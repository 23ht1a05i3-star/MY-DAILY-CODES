#Right angle triangle
rows = 5
#printing rows
for i in range(1, rows + 1):
    #printing the collumn
    for j in range(i):
        print("*", end="")
    #used for comming to new line
    print()  

#reverse right angle triangle
rows = 5
for i in range(rows, 0, -1):
    for j in range(i):
        print("*", end="")
    print()

#square paattern
rows = 5
for i in range(rows):
    for j in range(rows):
        print("*", end=" ")
    print()

#hallow square
rows = 5
for i in range(rows):
    for j in range(rows):
        if i == 0 or i == rows - 1 or j == 0 or j == rows - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

#piramid patterns
rows = 5
rows = 5
for i in range(1, rows + 1):
    # Print spaces
    for j in range(rows - i):
        print(" ", end="")
    # Print stars
    for k in range(i):
        print("*", end=" ")
    print()

#reverse that pyramid
rows = 5

for i in range(rows, 0, -1):

    for j in range(rows - i):
        print(" ", end="")
    for k in range(i):
        print("*", end=" ")
    print()

#Number Triangle
rows = 5
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

#Same Number Pattern print the rows
rows = 5
for i in range(1, rows + 1):
    for j in range(i):
        print(i, end=" ")
    print()

#Alpabatic triangle
rows = 5
for i in range(rows):
    for j in range(i + 1):
        print(chr(65 + j), end=" ")
    print()


#Hollow Triangle
n = 5
for i in range(1, n + 1):
    for j in range(1, 2 * n):
        if i == n or j == n-i+1 or j == n+i-1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

#0-1 Pattern
n = 5
for i in range(n):
    for j in range(i + 1):
        print((i + j) % 2, end=" ")
    print()

#Hollow Square
n = 5
for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

#X Pattern
n = 5
for i in range(n):
    for j in range(n):
        if i == j or i + j == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

#Plus Pattern
n = 5
mid = n // 2
for i in range(n):
    for j in range(n):
        if i == mid or j == mid:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

#Number Pyramid
n = 5
for i in range(1, n + 1):
    print(" " * (n-i), end="")
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

#Palindrome Number Pyramid
n = 5

for i in range(1, n + 1):
    print(" " * (n-i), end="")
    for j in range(1, i + 1):
        print(j, end="")
    for j in range(i - 1, 0, -1):
        print(j, end="")
    print()

#Pascal's Triangle
n = 5

for i in range(n):
    value = 1
    print(" " * (n-i), end="")
    for j in range(i + 1):
        print(value, end=" ")
        value = value * (i-j) // (j+1)
    print()