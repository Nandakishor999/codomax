# Module 1 — AI & Python Basics

Welcome to **Module 1: AI & Python Basics**.

This module introduces the fundamental concepts of **Artificial Intelligence** and builds the basic **Python programming skills** required for further learning in Machine Learning, Deep Learning, Generative AI, and AI application development.

---

## Learning Objectives

By completing this module, you will be able to:

* Understand the fundamentals of Artificial Intelligence.
* Explain the difference between AI, Machine Learning, and Deep Learning.
* Identify real-world applications of AI.
* Understand Python variables and data types.
* Work with input/output and operators.
* Use conditional statements.
* Work with loops and lists.
* Create and use Python functions.
* Build a small Python-based data analysis project.

---

## Module Structure

```text
module-1-ai-python-basics/
│
├── README.md
│
├── AI_Notes/
│   ├── introduction_to_ai.md
│   ├── ai_vs_ml_vs_dl.md
│   └── real_world_applications.md
│
├── Python_Basics/
│   ├── day1_basics.py
│   ├── day2_conditions.py
│   ├── day3_loops_lists.py
│   └── day4_functions.py
│
└── Mini_Project/
    └── student_performance_analyzer.py
```

---

# Part 1 — AI Fundamentals

The `AI_Notes` folder contains the theoretical foundation required before starting Machine Learning.

## 1. Introduction to AI

**File:**

```text
AI_Notes/introduction_to_ai.md
```

Topics covered:

* What is Artificial Intelligence?
* How AI works
* Major areas of AI
* Machine Learning
* Deep Learning
* Natural Language Processing
* Computer Vision
* Robotics
* Examples of AI systems

---

## 2. AI vs ML vs DL

**File:**

```text
AI_Notes/ai_vs_ml_vs_dl.md
```

This topic explains the relationship between:

```text
Artificial Intelligence
        │
        └── Machine Learning
                │
                └── Deep Learning
```

You will understand:

* What AI means
* What Machine Learning means
* What Deep Learning means
* Key differences between AI, ML, and DL
* Real-world examples

---

## 3. Real-World AI Applications

**File:**

```text
AI_Notes/real_world_applications.md
```

Applications covered include:

* Healthcare
* Finance
* Education
* E-commerce
* Transportation
* Cybersecurity
* Manufacturing
* Agriculture
* Customer service
* Generative AI

---

# Part 2 — Python Basics

The `Python_Basics` folder contains practical Python exercises.

## Day 1 — Python Basics

**File:**

```text
Python_Basics/day1_basics.py
```

Topics:

* Variables
* Data types
* Strings
* Integers
* Floats
* Booleans
* `input()`
* `print()`
* Arithmetic operators
* Basic calculations

Example:

```python
name = "Kishor"
age = 21

print("Name:", name)
print("Age:", age)
```

---

## Day 2 — Conditions

**File:**

```text
Python_Basics/day2_conditions.py
```

Topics:

* `if`
* `else`
* `elif`
* Comparison operators
* Logical operators
* Nested conditions
* Decision making

Example:

```python
marks = 85

if marks >= 40:
    print("Pass")
else:
    print("Fail")
```

---

## Day 3 — Loops and Lists

**File:**

```text
Python_Basics/day3_loops_lists.py
```

Topics:

* `for` loop
* `while` loop
* Lists
* List indexing
* `append()`
* `remove()`
* `len()`
* `max()`
* `min()`
* `sum()`
* `break`
* `continue`

Example:

```python
marks = [80, 75, 90, 85]

for mark in marks:
    print(mark)
```

---

## Day 4 — Functions

**File:**

```text
Python_Basics/day4_functions.py
```

Topics:

* Defining functions
* Function parameters
* Return values
* Default parameters
* Reusable code
* Functions with conditions

Example:

```python
def add(a, b):
    return a + b

result = add(10, 20)

print(result)
```

---

# Part 3 — Mini Project

## Student Performance Analyzer

**File:**

```text
Mini_Project/student_performance_analyzer.py
```

The **Student Performance Analyzer** is a beginner-friendly Python project that analyzes a student's academic performance.

### Features

The application calculates:

* Subject-wise marks
* Total marks
* Average marks
* Grade
* Pass/Fail status
* Highest mark
* Lowest mark

### Concepts Used

This project combines the concepts learned throughout the module:

```text
Variables
   ↓
Lists
   ↓
Loops
   ↓
Conditions
   ↓
Functions
   ↓
Basic Data Analysis
```

---

# How to Run the Project

## Step 1 — Install Python

Make sure Python 3 is installed.

Check the version:

```bash
python --version
```

or:

```bash
python3 --version
```

---

## Step 2 — Clone the Repository

```bash
git clone <YOUR-GITHUB-REPOSITORY-URL>
```

Move into the project directory:

```bash
cd module-1-ai-python-basics
```

---

## Step 3 — Run Python Lessons

### Day 1

```bash
python Python_Basics/day1_basics.py
```

### Day 2

```bash
python Python_Basics/day2_conditions.py
```

### Day 3

```bash
python Python_Basics/day3_loops_lists.py
```

### Day 4

```bash
python Python_Basics/day4_functions.py
```

---

## Step 4 — Run the Mini Project

```bash
python Mini_Project/student_performance_analyzer.py
```

Example interaction:

```text
Student Performance Analyzer

Enter student name: Kishor

Enter marks for Python: 85
Enter marks for SQL: 78
Enter marks for Machine Learning: 82
Enter marks for Mathematics: 75
Enter marks for English: 88
```

The program then generates a performance report containing the student's total, average, grade, and result.

---

# Learning Path

Follow the module in this order:

```text
1. Introduction to AI
        ↓
2. AI vs ML vs DL
        ↓
3. Real-World AI Applications
        ↓
4. Python Basics
        ↓
5. Conditions
        ↓
6. Loops & Lists
        ↓
7. Functions
        ↓
8. Student Performance Analyzer
```

---

# Skills Covered

### Artificial Intelligence

* AI Fundamentals
* AI Applications
* AI vs ML vs DL

### Python

* Variables
* Data Types
* Operators
* Input/Output
* Conditions
* Loops
* Lists
* Functions

### Problem Solving

* Logical thinking
* Basic data processing
* Program structure
* Reusable functions

---

# Project Goals

The main goal of this module is to build a strong foundation before moving into advanced AI topics.

After completing this module, you should be comfortable writing small Python programs and understanding the basic concepts behind Artificial Intelligence and Machine Learning.

---

# Future Learning

After completing Module 1, the recommended next step is:

```text
Module 1
AI + Python Basics
        ↓
Module 2
Python for Data Analysis
        ↓
Module 3
Statistics & Mathematics
        ↓
Module 4
Machine Learning
        ↓
Module 5
Deep Learning
        ↓
Module 6
Generative AI
        ↓
Module 7
RAG & LLM Applications
        ↓
Module 8
AI Engineering Projects
```

---

## Author

**Nandakishor Kalagarla**

B.Tech — CSE (AI & ML)

Focused on building practical skills in:

**Python • Machine Learning • Generative AI • RAG • LLMs • AI Application Development**

---

## License

This project is created for **learning, practice, and educational purposes**.
