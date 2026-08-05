# ==========================================
# STUDENT MANAGEMENT SYSTEM
# Today's Python Practice
# ==========================================

# Decorator
def logger(func):
    def wrapper(*args):
        print("\n==============================")
        print("Function:", func.__name__)
        result = func(*args)
        print("==============================")
        return result
    return wrapper


# Function 1
@logger
def student_details():
    name = input("Enter Student Name: ")
    roll = input("Enter Roll Number: ")

    print("\nStudent Details")
    print("Name :", name)
    print("Roll :", roll)


# Function 2
@logger
def calculate_result():
    marks = []

    for i in range(5):
        mark = int(input(f"Enter Subject {i+1} Marks: "))
        marks.append(mark)

    total = sum(marks)
    average = total / 5

    print("\nTotal :", total)
    print("Average :", average)

    if average >= 90:
        print("Grade : A")
    elif average >= 75:
        print("Grade : B")
    elif average >= 50:
        print("Grade : C")
    else:
        print("Fail")


# Function 3
@logger
def calculator():
    try:
        a = float(input("Enter First Number: "))
        b = float(input("Enter Second Number: "))

        print("\n1.Add")
        print("2.Subtract")
        print("3.Multiply")
        print("4.Divide")

        choice = input("Choose Operation: ")

        if choice == "1":
            print("Answer =", a + b)

        elif choice == "2":
            print("Answer =", a - b)

        elif choice == "3":
            print("Answer =", a * b)

        elif choice == "4":
            print("Answer =", a / b)

        else:
            print("Invalid Choice")

    except ZeroDivisionError:
        print("Cannot Divide by Zero")

    except ValueError:
        print("Invalid Input")


# Main Menu
while True:

    print("\n========== MENU ==========")
    print("1. Student Details")
    print("2. Student Result")
    print("3. Calculator")
    print("4. Exit")

    option = input("Enter Choice: ")

    if option == "1":
        student_details()

    elif option == "2":
        calculate_result()

    elif option == "3":
        calculator()

    elif option == "4":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")