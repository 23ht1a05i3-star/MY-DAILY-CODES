#printing the over all string in array
#slicing is for traversing the string
name = "Python Programming"
print(name[:])

#Starts from index 0 and stops before index 6.
name = "Python Programming"
print(name[0:6])

#Starts from index 7 and prints until the end.
name = "Python Programming"
#it includes spaces also
print(name[7:])

#Prints the first five characters.
name = "Python Programming"
print(name[:5])

#Print Last Character
#last index starting from negative neumbers
name = "Python"
print(name[-1])

#Prints the last three characters.
name = "Python"
print(name[-3:])

#Count Uppercase, Lowercase, Digits, and Special Characters
text = input("Enter a string: ")

upper = lower = digit = special = 0

for ch in text:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1
    elif ch.isdigit():
        digit += 1
    else:
        special += 1

print("Uppercase:", upper)
print("Lowercase:", lower)
print("Digits:", digit)
print("Special Characters:", special)

#Second Largest Word in a Sentence
text = input("Enter a sentence: ")
words = text.split()
words.sort(key=len)
print("Second Largest Word:", words[-2])

#String Compression
text = input("Enter a string: ")
count = 1
for i in range(len(text)-1):
    if text[i] == text[i+1]:
        count += 1
    else:
        print(text[i] + str(count), end="")
        count = 1
print(text[-1] + str(count))

#Check Anagram
a = input("First String: ")
b = input("Second String: ")
if sorted(a) == sorted(b):
    print("Anagram")
else:
    print("Not Anagram")

#everse Every Word
text = input("Enter Sentence: ")
words = text.split()
for word in words:
    print(word[::-1], end=" ")

#Count Frequency of Every Word
text = input("Enter Sentence: ")
words = text.lower().split()
for word in set(words):
    print(word, ":", words.count(word))

#Find Duplicate Characters
text = input("Enter String: ")

duplicate = ""
for ch in text:
    if text.count(ch) > 1 and ch not in duplicate:
        duplicate += ch
print("Duplicate Characters:", duplicate)

#Print the Most Frequent Character
text = input("Enter String: ")
max_char = ""
max_count = 0
for ch in text:
    if text.count(ch) > max_count:
        max_count = text.count(ch)
        max_char = ch
print("Most Frequent Character:", max_char)

#Check Whether Two Strings Are Rotations
a = input("First String: ")
b = input("Second String: ")
if len(a) == len(b) and b in a + a:
    print("Rotation")
else:
    print("Not Rotation")

#Convert to Title Case Without Using title()
text = input("Enter Sentence: ")
words = text.split()
for word in words:
    print(word[0].upper() + word[1:].lower(), end=" ")
