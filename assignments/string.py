# Program 1: Print numbers from 1 to 10 using a for loop
for i in range(1, 11):
    print(i, end=" ")
print()

# Program 2: Print numbers from 20 to 1 using a while loop
num = 20
while num >= 1:
    print(num, end=" ")
    num -= 1
print()

# Program 3: Print even numbers from 1 to 10
for i in range(1, 11):
    if i % 2 == 0:
        print(i, end=" ")
print()

# Program 4: Print numbers from 1 to n
n = int(input("Enter a number: "))
for i in range(1, n + 1):
    print(i, end=" ")
print()

# Program 5: Print odd numbers from 1 to n
n = int(input("Enter a number: "))
for i in range(1, n + 1):
    if i % 2 != 0:
        print(i, end=" ")
print()

# Program 6: Print 'Happy Birthday!' five times
for _ in range(5):
    print("Happy Birthday!")

# Program 7: Generate the first n terms of the series formed by squaring natural numbers
n = int(input("Enter a number: "))
print(f"The first {n} terms of the series are:")
for i in range(1, n + 1):
    print(i ** 2, end=" ")
print()

# Program 8: Print the multiplication table of a number
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

# Program 9: Print the first 8 terms of an arithmetic progression
start = 3
common_difference = 4
terms = 8
for i in range(terms):
    print(start + i * common_difference, end=" ")
print()

# Program 10: Print the first 6 terms of a geometric sequence
start = 2
common_ratio = 3
terms = 6
value = start
for _ in range(terms):
    print(value, end=" ")
    value *= common_ratio
print()

# Program 11: Calculate the sum of integers from 1 to n
n = int(input("Enter a positive integer: "))
total = sum(range(1, n + 1))
print(f"The sum of integers from 1 to {n} is: {total}")

# Program 12: Calculate the sum of reciprocals from 1 to n
n = int(input("Enter a positive integer: "))
reciprocal_sum = sum(1 / i for i in range(1, n + 1))
print(f"The sum of reciprocals from 1 to {n} is: {reciprocal_sum:.2f}")

# Program 13: Accumulate numbers entered by the user
running_total = 0
for _ in range(5):
    num = int(input("Enter a number: "))
    running_total += num
print(f"The final running total is: {running_total}")

# Program 14: Calculate the factorial of a number
n = int(input("Enter a positive integer: "))
if n < 0:
    print("Factorial does not exist for negative numbers.")
elif n == 0:
    print("The factorial of 0 is 1.")
else:
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    print(f"The factorial of {n} is {factorial}.")

# Program 15: Calculate power of a base to an exponent without ** or math.pow()
base = float(input("Enter the base number: "))
exponent = int(input("Enter the exponent: "))
result = 1
if exponent > 0:
    for _ in range(exponent):
        result *= base
elif exponent < 0:
    for _ in range(-exponent):
        result /= base
print(f"The result of {base} raised to the power of {exponent} is: {result}")

# Program 16: Count vowels in a string
string = input("Enter a string: ")
vowels = "aeiouAEIOU"
vowel_count = sum(1 for char in string if char in vowels)
print(f"Number of vowels in the string: {vowel_count}")

# Program 17: Count uppercase, lowercase, digits, and whitespace in a string
string = input("Enter a string: ")
uppercase_count = sum(1 for char in string if char.isupper())
lowercase_count = sum(1 for char in string if char.islower())
digit_count = sum(1 for char in string if char.isdigit())
whitespace_count = sum(1 for char in string if char.isspace())
print(f"Uppercase letters: {uppercase_count}")
print(f"Lowercase letters: {lowercase_count}")
print(f"Digits: {digit_count}")
print(f"Whitespace characters: {whitespace_count}")

# Program 18: Exchange first and last characters of a string
string = input("Enter a string: ")
if len(string) > 1:
    new_string = string[-1] + string[1:-1] + string[0]
else:
    new_string = string
print(f"New string: {new_string}")

# Program 19: Reverse a string
string = input("Enter a string: ")
reversed_string = "".join(reversed(string))
print(f"Reversed string: {reversed_string}")

# Program 20: Shift characters of a string to the left
string = input("Enter a string: ")
if len(string) > 1:
    shifted_string = string[1:] + string[0]
else:
    shifted_string = string
print(f"Shifted string: {shifted_string}")

# Program 21: Print initials of a name
name = input("Enter your full name (first middle last): ")
initials = "".join([name[0] + ". " if name[i - 1] == " " else "" for i in range(1, len(name)) if name[i] != " "]) + name[0] + "."
print(f"Initials: {initials}")

# Program 22: Check if a string is a palindrome
string = input("Enter a string: ")
is_palindrome = string == "".join(reversed(string))
print(f"The string is a palindrome: {is_palindrome}")

# Program 23: Display shifting pattern of "SHIFT"
word = "SHIFT"
for i in range(len(word)):
    print(word[i:] + word[:i])

# Program 24: Validate a password
password = input("Enter a password: ")
if (len(password) >= 8 and
    any(char.isupper() for char in password) and
    any(char.islower() for char in password) and
    any(char.isdigit() for char in password)):
    print("Password is valid.")
else:
    print("Password is invalid.")
