# ============================================================
# MINI PROJECT: STUDENT PERFORMANCE ANALYZER
# MODULE 1: AI & PYTHON BASICS
# ============================================================

"""
Project Description:
--------------------
Analyzes student marks and generates a performance report.

Passing Criteria:
-----------------
A student must score at least 35 marks in EVERY subject.

If even one subject has less than 35 marks:
    Result = FAIL
    Grade  = F

Otherwise, the grade is calculated based on the average.
"""


# ============================================================
# PASS MARK
# ============================================================

PASS_MARK = 35


# ============================================================
# 1. CALCULATE TOTAL
# ============================================================

def calculate_total(marks):
    return sum(marks)


# ============================================================
# 2. CALCULATE AVERAGE
# ============================================================

def calculate_average(marks):

    if len(marks) == 0:
        return 0

    return sum(marks) / len(marks)


# ============================================================
# 3. CHECK WHETHER STUDENT PASSED ALL SUBJECTS
# ============================================================

def check_result(marks):

    for mark in marks:

        if mark < PASS_MARK:
            return "FAIL"

    return "PASS"


# ============================================================
# 4. CALCULATE GRADE
# ============================================================

def calculate_grade(average, result):

    # If the student fails even one subject,
    # the final grade must be F.
    if result == "FAIL":
        return "F"

    # Grade based on average
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


# ============================================================
# 5. FIND FAILED SUBJECTS
# ============================================================

def find_failed_subjects(subjects, marks):

    failed_subjects = []

    for subject, mark in zip(subjects, marks):

        if mark < PASS_MARK:
            failed_subjects.append(subject)

    return failed_subjects


# ============================================================
# 6. DISPLAY REPORT
# ============================================================

def display_report(name, subjects, marks):

    total = calculate_total(marks)

    average = calculate_average(marks)

    result = check_result(marks)

    grade = calculate_grade(average, result)

    highest = max(marks)

    lowest = min(marks)

    failed_subjects = find_failed_subjects(subjects, marks)


    print("\n")
    print("=" * 55)
    print("           STUDENT PERFORMANCE REPORT")
    print("=" * 55)

    print("Student Name :", name)

    print("\nSubject-wise Marks")
    print("-" * 55)

    for subject, mark in zip(subjects, marks):

        status = "PASS" if mark >= PASS_MARK else "FAIL"

        print(
            f"{subject:<25} {mark:>7.2f}    {status}"
        )

    print("-" * 55)

    print(f"{'Total Marks':<25} {total:>7.2f}")

    print(f"{'Average Marks':<25} {average:>7.2f}")

    print(f"{'Highest Mark':<25} {highest:>7.2f}")

    print(f"{'Lowest Mark':<25} {lowest:>7.2f}")

    print(f"{'Grade':<25} {grade:>7}")

    print(f"{'Result':<25} {result:>7}")


    # Show failed subjects
    if result == "FAIL":

        print("\nFailed Subject(s):")

        for subject in failed_subjects:

            index = subjects.index(subject)

            print(
                f"- {subject}: "
                f"{marks[index]:.2f} marks "
                f"(Pass Mark: {PASS_MARK})"
            )

    print("=" * 55)


# ============================================================
# 7. MAIN PROGRAM
# ============================================================

def main():

    print("=" * 55)
    print("          STUDENT PERFORMANCE ANALYZER")
    print("=" * 55)

    print(f"\nMinimum pass mark for each subject: {PASS_MARK}")

    # Student name
    student_name = input("\nEnter student name: ")


    # Subjects
    subjects = [
        "Python",
        "SQL",
        "Machine Learning",
        "Mathematics",
        "English"
    ]


    marks = []


    # Get marks
    print("\nEnter marks between 0 and 100.")

    for subject in subjects:

        while True:

            try:

                mark = float(
                    input(f"Enter marks for {subject}: ")
                )

                if 0 <= mark <= 100:

                    marks.append(mark)

                    break

                else:

                    print(
                        "Invalid marks. "
                        "Enter a value between 0 and 100."
                    )

            except ValueError:

                print(
                    "Please enter a valid number."
                )


    # Display report
    display_report(
        student_name,
        subjects,
        marks
    )


# ============================================================
# 8. PROGRAM ENTRY POINT
# ============================================================

if __name__ == "__main__":

    main()