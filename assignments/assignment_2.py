#1. Area of a Rectangle


length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
area = length * width
print(f"The area of the rectangle is: {area}")
#2. Circumference of a Circle

import math
radius = float(input("Enter the radius of the circle: "))
circumference = 2 * math.pi * radius
print(f"The circumference of the circle is: {circumference}")


#3. Simple Interest

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate (in %): ")) / 100
time = float(input("Enter the time (in years): "))
simple_interest = principal * rate * time
print(f"The simple interest is: {simple_interest}")


#4. Speed of an Object

distance = float(input("Enter the distance traveled (in meters): "))
time = float(input("Enter the time taken (in seconds): "))
speed = distance / time
print(f"The speed of the object is: {speed} m/s")


#5. BMI Calculator

weight = float(input("Enter your weight (in kilograms): "))
height = float(input("Enter your height (in meters): "))
bmi = weight / (height ** 2)
print(f"Your Body Mass Index (BMI) is: {bmi}")

#6. Force Using Newton's Second Law

mass = float(input("Enter the mass (in kilograms): "))
acceleration = float(input("Enter the acceleration (in m/s²): "))
force = mass * acceleration
print(f"The force is: {force} N")

#7. Compound Interest

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate (in %): ")) / 100
times_compounded = int(input("Enter the number of times interest is compounded per year: "))
time = float(input("Enter the time (in years): "))
amount = principal * (1 + rate / times_compounded) ** (times_compounded * time)
print(f"The total amount after compound interest is: {amount}")


#8. Perimeter of a Triangle

a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))
c = float(input("Enter the length of side c: "))
perimeter = a + b + c
print(f"The perimeter of the triangle is: {perimeter}")


#9. Volume of a Sphere

radius = float(input("Enter the radius of the sphere: "))
volume = (4 / 3) * math.pi * (radius ** 3)
print(f"The volume of the sphere is: {volume}")


#10. Kinetic Energy

mass = float(input("Enter the mass of the object (in kilograms): "))
velocity = float(input("Enter the velocity of the object (in m/s): "))
kinetic_energy = 0.5 * mass * (velocity ** 2)
print(f"The kinetic energy of the object is: {kinetic_energy} J")


#11. Quadratic Equation Roots

import cmath
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))
discriminant = cmath.sqrt(b**2 - 4*a*c)
root1 = (-b + discriminant) / (2 * a)
root2 = (-b - discriminant) / (2 * a)
print(f"The roots of the quadratic equation are: {root1} and {root2}")


#12. Temperature Conversion

celsius = float(input("Enter the temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"The temperature in Fahrenheit is: {fahrenheit}")


#13. Gravitational Force

G = 6.674 * 10**-11
m1 = float(input("Enter the mass of the first object (in kg): "))
m2 = float(input("Enter the mass of the second object (in kg): "))
r = float(input("Enter the distance between the objects (in meters): "))
force = G * (m1 * m2) / (r ** 2)
print(f"The gravitational force is: {force} N")


#14. Volume of a Cylinder

radius = float(input("Enter the radius of the cylinder: "))
height = float(input("Enter the height of the cylinder: "))
volume = math.pi * (radius ** 2) * height
print(f"The volume of the cylinder is: {volume}")


#15. Pressure

force = float(input("Enter the force (in Newtons): "))
area = float(input("Enter the area (in square meters): "))
pressure = force / area
print(f"The pressure is: {pressure} Pa")


#16. Electric Power

voltage = float(input("Enter the voltage (in Volts): "))
current = float(input("Enter the current (in Amperes): "))
power = voltage * current
print(f"The electric power is: {power} W")


#17. Perimeter of a Circle

radius = float(input("Enter the radius of the circle: "))
perimeter = 2 * math.pi * radius
print(f"The perimeter of the circle is: {perimeter}")



#18. Future Value in Savings

present_value = float(input("Enter the present value: "))
rate = float(input("Enter the annual interest rate (in %): ")) / 100
time = float(input("Enter the time (in years): "))
future_value = present_value * (1 + rate) ** time
print(f"The future value is: {future_value}")



#19. Work Done by a Force

import math
force = float(input("Enter the force (in Newtons): "))
distance = float(input("Enter the distance (in meters): "))
theta = float(input("Enter the angle (in degrees): "))
work_done = force * distance * math.cos(math.radians(theta))
print(f"The work done is: {work_done} J")


#20. Heat Transfer

mass = float(input("Enter the mass (in kilograms): "))
specific_heat = float(input("Enter the specific heat capacity (in J/kg°C): "))
delta_temp = float(input("Enter the temperature change (in °C): "))
heat_transfer = mass * specific_heat * delta_temp
print(f"The heat transferred is: {heat_transfer} J")