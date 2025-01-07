# Program 1: Check if a number is even or odd
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

# Program 2: Check voting eligibility
age = int(input("\nEnter your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote yet.")

# Program 3: Find the largest of two numbers
num1 = int(input("\nEnter the first number: "))
num2 = int(input("Enter the second number: "))
print(f"The largest number is {max(num1, num2)}.")

# Program 4: Check if a number is positive, negative, or zero
num = int(input("\nEnter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

# Program 5: Determine age group
age = int(input("\nEnter your age: "))
if age <= 12:
    print("Child")
elif 13 <= age <= 19:
    print("Teenager")
elif 20 <= age <= 59:
    print("Adult")
else:
    print("Senior Citizen")

# Program 6: Display day of the week
day = int(input("\nEnter a number (1-7): "))
days = {1: "Sunday", 2: "Monday", 3: "Tuesday", 4: "Wednesday", 5: "Thursday", 6: "Friday", 7: "Saturday"}
print(days.get(day, "Error: Number must be between 1 and 7."))

# Program 7: Calculate BMI
weight = float(input("\nEnter your weight (kg): "))
height = float(input("Enter your height (m): "))
bmi = weight / (height ** 2)
if bmi < 18.5:
    print("Underweight")
elif 18.5 <= bmi <= 24.9:
    print("Normal weight")
elif 25 <= bmi <= 29.9:
    print("Overweight")
else:
    print("Obesity")

# Program 8: Calculate grade based on average marks
marks = [float(input(f"\nEnter marks for subject {i+1}: ")) for i in range(3)]
average = sum(marks) / 3
if 90 <= average <= 100:
    grade = "A"
elif 80 <= average < 90:
    grade = "B"
elif 70 <= average < 80:
    grade = "C"
elif 60 <= average < 70:
    grade = "D"
else:
    grade = "F"
print(f"Average: {average:.2f}, Grade: {grade}")

# Program 9: Solve quadratic equation
import math
a = float(input("\nEnter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))
discriminant = b**2 - 4*a*c
if discriminant > 0:
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    print(f"Two real roots: {root1}, {root2}")
elif discriminant == 0:
    root = -b / (2*a)
    print(f"One real root: {root}")
else:
    real_part = -b / (2*a)
    imag_part = math.sqrt(-discriminant) / (2*a)
    print(f"Two complex roots: {real_part} + {imag_part}i, {real_part} - {imag_part}i")

# Program 10: Sort three numbers
nums = [float(input("\nEnter number: ")) for _ in range(3)]
print("Sorted numbers:", sorted(nums))

# Program 11: Find the largest of three numbers
nums = [float(input("\nEnter number: ")) for _ in range(3)]
print("Largest number:", max(nums))

# Program 12: Check if character is vowel or consonant
char = input("\nEnter a character: ").lower()
if char in 'aeiou':
    print("Vowel")
elif char.isalpha():
    print("Consonant")
else:
    print("Invalid input")

# Program 13: Check if a year is a leap year
year = int(input("\nEnter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")

# Program 14: Calculate telephone bill
calls = int(input("\nEnter number of calls: "))
if calls <= 100:
    bill = 200
elif calls <= 150:
    bill = 200 + (calls - 100) * 0.60
elif calls <= 200:
    bill = 200 + 50 * 0.60 + (calls - 150) * 0.50
else:
    bill = 200 + 50 * 0.60 + 50 * 0.50 + (calls - 200) * 0.40
print(f"Total bill: Rs. {bill:.2f}")
