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
