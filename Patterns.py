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