# DAY 1: PYTHON BASICS

"""
Day 1 Objectives:
1. Understand Python syntax
2. Learn variables
3. Learn basic data types
4. Use print() and input()
5. Understand type conversion
6. Practice arithmetic operators
7. Build simple Python programs
"""


# 1. PRINTING OUTPUT

print("Hello, World!")
print("Welcome to Python Programming")
print("I am learning Python for AI Engineering")


# 2. VARIABLES

name = "Nandakishor"
age = 21
course = "B.Tech CSE - AI & ML"
cgpa = 7.77

print("\n--- Student Information ---")
print("Name:", name)
print("Age:", age)
print("Course:", course)
print("CGPA:", cgpa)


# 3. BASIC DATA TYPES

student_name = "Kishor"     # String
student_age = 21            # Integer
student_cgpa = 7.77         # Float
is_student = True           # Boolean

print("\n--- Data Types ---")
print(type(student_name))
print(type(student_age))
print(type(student_cgpa))
print(type(is_student))


# 4. TAKING USER INPUT

print("\n--- User Input ---")

user_name = input("Enter your name: ")

print("Hello", user_name)


# 5. TYPE CONVERSION

print("\n--- Type Conversion ---")

age = int(input("Enter your age: "))
height = float(input("Enter your height in cm: "))

print("Your age is:", age)
print("Your height is:", height, "cm")


# 6. ARITHMETIC OPERATORS

print("\n--- Arithmetic Operators ---")

a = 20
b = 5

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Power:", a ** b)


# 7. SIMPLE CALCULATOR

print("\n--- Simple Calculator ---")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)

if num2 != 0:
    print("Division:", num1 / num2)
else:
    print("Division is not possible by zero.")


# 8. STUDENT MARKS CALCULATION

print("\n--- Student Marks Calculator ---")

python_marks = float(input("Enter Python marks: "))
sql_marks = float(input("Enter SQL marks: "))
ai_marks = float(input("Enter AI marks: "))

total_marks = python_marks + sql_marks + ai_marks
average_marks = total_marks / 3

print("Total Marks:", total_marks)
print("Average Marks:", average_marks)


# 9. F-STRING

print("\n--- Formatted Output ---")

student = "Nandakishor"
branch = "CSE - AI & ML"

print(f"Student Name: {student}")
print(f"Branch: {branch}")
print(f"Age: {age}")


# 10. DAY 1 PRACTICE TASKS

"""
Practice Task 1:
Create variables for:
    Name
    Age
    College
    Branch
    CGPA

Display all the information.

Practice Task 2:
Take two numbers from the user and calculate:
    Addition
    Subtraction
    Multiplication
    Division

Practice Task 3:
Calculate the area of a rectangle.

Formula:
    Area = Length × Width

Practice Task 4:
Convert Celsius into Fahrenheit.

Formula:
    Fahrenheit = (Celsius × 9/5) + 32

Practice Task 5:
Calculate simple interest.

Formula:
    SI = (Principal × Rate × Time) / 100

Practice Task 6:
Take marks of 5 subjects and calculate:
    Total
    Average

Practice Task 7:
Calculate BMI.

Formula:
    BMI = Weight / (Height × Height)
"""


# ============================================================
# DAY 1 COMPLETED
# ============================================================

print("\n===================================")
print("DAY 1 PYTHON BASICS COMPLETED")
print("===================================")