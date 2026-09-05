print("==========================================")
print("DAY 4 - PYTHON FUNCTIONS")
print("==========================================")


print("\n---- BASIC FUNCTION ----")


def greet():
    print("Hello, welcome to Python!")


greet()


print("\n---- FUNCTION WITH PARAMETER ----")


def greet_user(name):
    print(f"Hello, {name}!")


greet_user("Nandakishor")
greet_user("Rahul")


print("\n---- FUNCTION WITH MULTIPLE PARAMETERS ----")


def introduce(name, age, course):
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Course: {course}")


introduce("Nandakishor", 21, "B.Tech CSE - AI & ML")


print("\n---- FUNCTION WITH RETURN VALUE ----")


def add(a, b):
    return a + b


result = add(10, 20)

print("Result:", result)


print("\n---- SUBTRACTION ----")


def subtract(a, b):
    return a - b


result = subtract(50, 20)

print("Result:", result)


print("\n---- MULTIPLICATION ----")


def multiply(a, b):
    return a * b


result = multiply(10, 5)

print("Result:", result)


print("\n---- DIVISION ----")


def divide(a, b):

    if b == 0:
        return "Cannot divide by zero."

    return a / b


result = divide(20, 5)

print("Result:", result)


print("\n---- FUNCTION WITH CONDITION ----")


def check_number(number):

    if number > 0:
        return "Positive"

    elif number < 0:
        return "Negative"

    else:
        return "Zero"


print(check_number(10))
print(check_number(-5))
print(check_number(0))


print("\n---- EVEN OR ODD FUNCTION ----")


def check_even_odd(number):

    if number % 2 == 0:
        return "Even"

    else:
        return "Odd"


print("10:", check_even_odd(10))
print("7:", check_even_odd(7))


print("\n---- PASS OR FAIL FUNCTION ----")


def check_pass(mark):

    if mark >= 35:
        return "PASS"

    else:
        return "FAIL"


print("Mark 80:", check_pass(80))
print("Mark 25:", check_pass(25))


print("\n---- STUDENT GRADE FUNCTION ----")


def calculate_grade(average):

    if average >= 90:
        return "A+"

    elif average >= 80:
        return "A"

    elif average >= 70:
        return "B"

    elif average >= 60:
        return "C"

    elif average >= 50:
        return "D"

    else:
        return "F"


print("Average 95:", calculate_grade(95))
print("Average 85:", calculate_grade(85))
print("Average 75:", calculate_grade(75))
print("Average 65:", calculate_grade(65))
print("Average 55:", calculate_grade(55))
print("Average 30:", calculate_grade(30))


print("\n---- FUNCTION WITH LIST ----")


def calculate_total(marks):
    return sum(marks)


marks = [80, 75, 90, 85, 70]

total = calculate_total(marks)

print("Marks:", marks)
print("Total:", total)


print("\n---- AVERAGE FUNCTION ----")


def calculate_average(marks):

    if len(marks) == 0:
        return 0

    return sum(marks) / len(marks)


average = calculate_average(marks)

print("Average:", average)


print("\n---- HIGHEST AND LOWEST MARK ----")


def find_highest(marks):
    return max(marks)


def find_lowest(marks):
    return min(marks)


print("Highest:", find_highest(marks))
print("Lowest:", find_lowest(marks))


print("\n---- COUNT PASS AND FAIL ----")


def count_results(marks):

    passed = 0
    failed = 0

    for mark in marks:

        if mark >= 35:
            passed += 1

        else:
            failed += 1

    return passed, failed


student_marks = [80, 25, 75, 90, 30, 65]

passed, failed = count_results(student_marks)

print("Marks:", student_marks)
print("Passed:", passed)
print("Failed:", failed)


print("\n---- DEFAULT PARAMETER ----")


def welcome(name="Student"):
    print(f"Welcome, {name}!")


welcome()
welcome("Nandakishor")


print("\n---- FUNCTION WITH USER INPUT ----")


def square(number):
    return number * number


number = float(input("Enter a number: "))

print("Square:", square(number))


print("\n---- SIMPLE CALCULATOR FUNCTION ----")


def calculator(a, b, operator):

    if operator == "+":
        return a + b

    elif operator == "-":
        return a - b

    elif operator == "*":
        return a * b

    elif operator == "/":

        if b == 0:
            return "Cannot divide by zero."

        return a / b

    else:
        return "Invalid operator."


num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

result = calculator(num1, num2, operator)

print("Result:", result)


print("\n---- STUDENT PERFORMANCE FUNCTION ----")


def student_performance(name, marks):

    total = sum(marks)

    average = total / len(marks)

    if any(mark < 35 for mark in marks):
        result = "FAIL"
        grade = "F"

    else:
        result = "PASS"
        grade = calculate_grade(average)

    return total, average, grade, result


student_name = "Nandakishor"

student_marks = [77, 80, 35, 90, 99]

total, average, grade, result = student_performance(
    student_name,
    student_marks
)

print("Student:", student_name)
print("Marks:", student_marks)
print("Total:", total)
print("Average:", average)
print("Grade:", grade)
print("Result:", result)


print("\n---- DAY 4 PRACTICE TASKS ----")

print("""
Practice Task 1:
Create a function to calculate the area of a rectangle.

Practice Task 2:
Create a function to calculate the area of a circle.

Practice Task 3:
Create a function to check whether a number is prime.

Practice Task 4:
Create a function to find the largest number
from a list.

Practice Task 5:
Create a function to calculate the average
of student marks.

Practice Task 6:
Create a function to check PASS or FAIL.
Pass mark = 35.

Practice Task 7:
Create a function that converts Celsius
to Fahrenheit.

Practice Task 8:
Create a calculator using functions.

Practice Task 9:
Create a function to count even and odd
numbers in a list.

Practice Task 10:
Create a student performance analyzer using
multiple functions.
""")


print("==========================================")
print("DAY 4 - FUNCTIONS COMPLETED")
print("==========================================")