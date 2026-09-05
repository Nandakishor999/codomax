# ============================================================
# MODULE 1: AI & PYTHON BASICS
# DAY 3: LOOPS AND LISTS
# ============================================================

"""
Day 3 Objectives:
1. Understand loops
2. Learn for loops
3. Learn while loops
4. Use range()
5. Understand lists
6. Access list elements using indexes
7. Add and remove list elements
8. Loop through lists
9. Use break and continue
10. Perform basic operations on lists
"""


# ============================================================
# 1. FOR LOOP
# ============================================================

print("---- FOR LOOP ----")

for number in range(1, 6):
    print(number)


# ============================================================
# 2. FOR LOOP WITH STRINGS
# ============================================================

print("\n---- LOOP THROUGH A STRING ----")

name = "Kishor"

for character in name:
    print(character)


# ============================================================
# 3. RANGE() FUNCTION
# ============================================================

print("\n---- RANGE FUNCTION ----")

# Numbers from 0 to 4
for number in range(5):
    print(number)

print("\nNumbers from 1 to 10:")

for number in range(1, 11):
    print(number)


# ============================================================
# 4. EVEN NUMBERS USING FOR LOOP
# ============================================================

print("\n---- EVEN NUMBERS ----")

for number in range(1, 21):

    if number % 2 == 0:
        print(number)


# ============================================================
# 5. ODD NUMBERS USING FOR LOOP
# ============================================================

print("\n---- ODD NUMBERS ----")

for number in range(1, 21):

    if number % 2 != 0:
        print(number)


# ============================================================
# 6. WHILE LOOP
# ============================================================

print("\n---- WHILE LOOP ----")

count = 1

while count <= 5:

    print(count)

    count += 1


# ============================================================
# 7. COUNTDOWN USING WHILE LOOP
# ============================================================

print("\n---- COUNTDOWN ----")

count = 5

while count >= 1:

    print(count)

    count -= 1

print("Start!")


# ============================================================
# 8. SUM OF NUMBERS
# ============================================================

print("\n---- SUM OF NUMBERS ----")

total = 0

for number in range(1, 11):

    total += number

print("Sum:", total)


# ============================================================
# 9. MULTIPLICATION TABLE
# ============================================================

print("\n---- MULTIPLICATION TABLE ----")

number = int(input("Enter a number: "))

for i in range(1, 11):

    result = number * i

    print(f"{number} x {i} = {result}")


# ============================================================
# 10. LIST BASICS
# ============================================================

print("\n---- LIST BASICS ----")

marks = [77, 80, 22, 90, 99]

print("Marks:", marks)

print("First mark:", marks[0])

print("Second mark:", marks[1])

print("Last mark:", marks[-1])


# ============================================================
# 11. LIST LENGTH
# ============================================================

print("\n---- LIST LENGTH ----")

print("Number of subjects:", len(marks))


# ============================================================
# 12. ADDING ITEMS TO A LIST
# ============================================================

print("\n---- ADDING ITEMS ----")

marks.append(85)

print("Updated marks:", marks)


# ============================================================
# 13. INSERTING ITEMS
# ============================================================

print("\n---- INSERT ITEM ----")

marks.insert(1, 88)

print("Updated marks:", marks)


# ============================================================
# 14. REMOVING ITEMS
# ============================================================

print("\n---- REMOVE ITEM ----")

marks.remove(22)

print("Updated marks:", marks)


# ============================================================
# 15. POP METHOD
# ============================================================

print("\n---- POP METHOD ----")

removed_mark = marks.pop()

print("Removed mark:", removed_mark)

print("Updated marks:", marks)


# ============================================================
# 16. LOOP THROUGH A LIST
# ============================================================

print("\n---- LOOP THROUGH LIST ----")

marks = [77, 80, 22, 90, 99]

for mark in marks:

    print(mark)


# ============================================================
# 17. FIND PASSING MARKS
# ============================================================

print("\n---- PASSING MARKS ----")

for mark in marks:

    if mark >= 35:
        print(mark)


# ============================================================
# 18. FIND FAILED MARKS
# ============================================================

print("\n---- FAILED MARKS ----")

for mark in marks:

    if mark < 35:
        print(mark)


# ============================================================
# 19. MAXIMUM AND MINIMUM
# ============================================================

print("\n---- MAXIMUM AND MINIMUM ----")

print("Highest mark:", max(marks))

print("Lowest mark:", min(marks))


# ============================================================
# 20. TOTAL AND AVERAGE
# ============================================================

print("\n---- TOTAL AND AVERAGE ----")

total = sum(marks)

average = total / len(marks)

print("Total:", total)

print("Average:", average)


# ============================================================
# 21. SORTING A LIST
# ============================================================

print("\n---- SORTING ----")

marks = [77, 80, 22, 90, 99]

marks.sort()

print("Ascending order:", marks)

marks.sort(reverse=True)

print("Descending order:", marks)


# ============================================================
# 22. LIST SLICING
# ============================================================

print("\n---- LIST SLICING ----")

numbers = [10, 20, 30, 40, 50]

print("Complete list:", numbers)

print("First three:", numbers[:3])

print("Last two:", numbers[-2:])

print("Middle elements:", numbers[1:4])


# ============================================================
# 23. BREAK STATEMENT
# ============================================================

print("\n---- BREAK ----")

for number in range(1, 11):

    if number == 6:
        break

    print(number)


# ============================================================
# 24. CONTINUE STATEMENT
# ============================================================

print("\n---- CONTINUE ----")

for number in range(1, 11):

    if number == 6:
        continue

    print(number)


# ============================================================
# 25. SEARCH AN ITEM IN A LIST
# ============================================================

print("\n---- SEARCH IN LIST ----")

students = [
    "Kishor",
    "Rahul",
    "Priya",
    "Anjali"
]

search_name = input("Enter student name to search: ")

if search_name in students:
    print(search_name, "is present in the list.")
else:
    print(search_name, "is not present in the list.")


# ============================================================
# 26. STUDENT MARKS ANALYSIS
# ============================================================

print("\n---- STUDENT MARKS ANALYSIS ----")

student_marks = [85, 72, 91, 68, 77, 95, 32]

passed = 0
failed = 0

for mark in student_marks:

    if mark >= 35:
        passed += 1
    else:
        failed += 1

print("Marks:", student_marks)

print("Passed subjects:", passed)

print("Failed subjects:", failed)

print("Highest mark:", max(student_marks))

print("Lowest mark:", min(student_marks))

print("Average:", sum(student_marks) / len(student_marks))


# ============================================================
# 27. NESTED LOOP
# ============================================================

print("\n---- NESTED LOOP ----")

for row in range(1, 4):

    for column in range(1, 4):

        print("*", end=" ")

    print()

# DAY 3 COMPLETED


print("\n==========================================")
print("DAY 3 - LOOPS AND LISTS COMPLETED")
print("==========================================")