#Count Vowels and Consonants
text = input("Enter a string: ")

vowels = 0
consonants = 0

for ch in text.lower():
    if ch.isalpha():
        if ch in "aeiou":
            vowels += 1
        else:
            consonants += 1

print("Vowels:", vowels)
print("Consonants:", consonants)

#Reverse a Number
num = int(input("Enter number: "))
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10
print("Reverse:", reverse)

#Palindrome Number
num = input("Enter number: ")
if num == num[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

#Count Digits
num = int(input("Enter number: "))
count = 0

while num > 0:
    num //= 10
    count += 1
print("Digits:", count)

#umof Digits
num = int(input("Enter number: "))
total = 0
while num > 0:
    total += num % 10
    num //= 10
print("Sum:", total)

#Armstrong Number
num = int(input("Enter number: "))
temp = num
total = 0
while temp > 0:
    digit = temp % 10
    total += digit ** 3
    temp //= 10
if total == num:
    print("Armstrong Number")
else:
    print("Not Armstrong")