# ============================================================
# MODULE 1: AI & PYTHON BASICS
# DAY 2: CONDITIONAL STATEMENTS
# ============================================================

"""
Day 2 Objectives:
1. Understand conditional statements
2. Learn if, elif and else
3. Use comparison operators
4. Use logical operators
5. Understand nested conditions
6. Practice decision-making programs
"""


# ============================================================
# 1. BASIC IF STATEMENT
# ============================================================

print("---- Basic IF Statement ----")

age = 20

if age >= 18:
    print("You are eligible to vote.")


# ============================================================
# 2. IF-ELSE STATEMENT
# ============================================================

print("\n---- IF-ELSE Statement ----")

number = 10

if number > 0:
    print("The number is positive.")
else:
    print("The number is not positive.")


# ============================================================
# 3. EVEN OR ODD
# ============================================================

print("\n---- Even or Odd ----")

number = int(input("Enter a number: "))

if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")


# ============================================================
# 4. IF-ELIF-ELSE
# ============================================================

print("\n---- IF-ELIF-ELSE ----")

marks = float(input("Enter your marks: "))

if marks >= 90:
    print("Grade: A+")
elif marks >= 80:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
elif marks >= 50:
    print("Grade: D")
else:
    print("Grade: F")


# ============================================================
# 5. PASS OR FAIL
# ============================================================

print("\n---- Pass or Fail ----")

marks = float(input("Enter your marks: "))

if marks >= 40:
    print("Result: PASS")
else:
    print("Result: FAIL")


# ============================================================
# 6. COMPARISON OPERATORS
# ============================================================

print("\n---- Comparison Operators ----")

a = 20
b = 10

print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)


# ============================================================
# 7. LOGICAL OPERATORS
# ============================================================

print("\n---- Logical Operators ----")

age = 22
has_id = True

# AND
if age >= 18 and has_id:
    print("AND: Both conditions are true.")

# OR
if age >= 18 or has_id:
    print("OR: At least one condition is true.")

# NOT
is_student = False

if not is_student:
    print("NOT: The person is not a student.")


# ============================================================
# 8. LARGEST OF TWO NUMBERS
# ============================================================

print("\n---- Largest of Two Numbers ----")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if num1 > num2:
    print("Largest number:", num1)
elif num2 > num1:
    print("Largest number:", num2)
else:
    print("Both numbers are equal.")


# ============================================================
# 9. LARGEST OF THREE NUMBERS
# ============================================================

print("\n---- Largest of Three Numbers ----")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

if num1 >= num2 and num1 >= num3:
    print("Largest number:", num1)
elif num2 >= num1 and num2 >= num3:
    print("Largest number:", num2)
else:
    print("Largest number:", num3)


# ============================================================
# 10. VOTING ELIGIBILITY
# ============================================================

print("\n---- Voting Eligibility ----")

age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")


# ============================================================
# 11. LOGIN CHECK
# ============================================================

print("\n---- Login Check ----")

correct_username = "admin"
correct_password = "python123"

username = input("Enter username: ")
password = input("Enter password: ")

if username == correct_username and password == correct_password:
    print("Login successful.")
else:
    print("Invalid username or password.")


# ============================================================
# 12. POSITIVE, NEGATIVE OR ZERO
# ============================================================

print("\n---- Number Classification ----")

number = float(input("Enter a number: "))

if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")


# ============================================================
# 13. NESTED IF STATEMENT
# ============================================================

print("\n---- Nested IF Statement ----")

age = int(input("Enter your age: "))
has_license = input("Do you have a driving license? (yes/no): ")

if age >= 18:
    if has_license.lower() == "yes":
        print("You are eligible to drive.")
    else:
        print("You need a driving license.")
else:
    print("You must be 18 or older to drive.")


# ============================================================
# 14. SIMPLE CALCULATOR USING CONDITIONS
# ============================================================

print("\n---- Simple Calculator ----")

num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

if operator == "+":
    print("Result:", num1 + num2)

elif operator == "-":
    print("Result:", num1 - num2)

elif operator == "*":
    print("Result:", num1 * num2)

elif operator == "/":
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Cannot divide by zero.")

else:
    print("Invalid operator.")


# ============================================================
# 15. STUDENT GRADE CHECK
# ============================================================

print("\n---- Student Grade Check ----")

student_name = input("Enter student name: ")
marks = float(input("Enter marks: "))

if marks < 0 or marks > 100:
    print("Invalid marks.")

elif marks >= 90:
    print(student_name, "- Grade A+")

elif marks >= 80:
    print(student_name, "- Grade A")

elif marks >= 70:
    print(student_name, "- Grade B")

elif marks >= 60:
    print(student_name, "- Grade C")

elif marks >= 40:
    print(student_name, "- Grade D")

else:
    print(student_name, "- Grade F")


# ============================================================
# DAY 2 PRACTICE TASKS
# ============================================================

"""
Practice Task 1:
Write a program to check whether a number is positive,
negative, or zero.


Practice Task 2:
Write a program to check whether a number is even or odd.


Practice Task 3:
Write a program to find the largest of two numbers.


Practice Task 4:
Write a program to find the largest of three numbers.


Practice Task 5:
Write a program to check whether a person is eligible
to vote.


Practice Task 6:
Create a grading system:

    90 - 100  -> A+
    80 - 89   -> A
    70 - 79   -> B
    60 - 69   -> C
    40 - 59   -> D
    Below 40  -> F


Practice Task 7:
Create a simple calculator using:

    +
    -
    *
    /


Practice Task 8:
Write a program to check whether a year is a leap year.


Practice Task 9:
Write a program to check whether a person is eligible
for a driving license based on age.


Practice Task 10:
Create a login system using username and password.


Practice Task 11:
Write a program to calculate discount:

    If price >= 5000  -> 20% discount
    If price >= 3000  -> 10% discount
    Otherwise         -> No discount


Practice Task 12:
Create a student result system that accepts marks
for three subjects.

The student passes only if all three subjects
have marks >= 40.
"""


# ============================================================
# DAY 2 COMPLETED
# ============================================================

print("\n===================================")
print("DAY 2 CONDITIONS COMPLETED")
print("===================================")