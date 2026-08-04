#fine the  user enter number is even or odd
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")

#num = int(input("Enter a number: ")) this line is used to take  the input from the user
#num%2==0 used tocheck the number is even or odd
#if even print even number else oddnumber

#Checking for leep year
year = int(input("Enter a year: "))
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not a Leap Year")

#Check Divisible by 5
num = int(input("Enter a number: "))
if num % 5 == 0:
    print("Divisible by 5")
else:
    print("Not Divisible by 5")

#Check Divisible by 5 and 11
num = int(input("Enter a number: "))
if num % 5 == 0 and num % 11 == 0:
    print("Divisible by 5 and 11")
else:
    print("Not Divisible by 5 and 11")

#Check Alphabet or Not
ch = input("Enter a character: ")
if ('a' <= ch <= 'z') or ('A' <= ch <= 'Z'):
    print("Alphabet")
else:
    print("Not an Alphabet")

#Checking owels ornot
ch = input("Enter an alphabet: ")
if ch in "aeiouAEIOU":
    print("Vowel")
else:
    print("Consonant")

    