"""
=====================================================
MODULE 2 - PYTHON MINI PROJECT
Expense Tracker Application
Author: Nandakishor Kalagarla
B.Tech - CSE (AI & ML)
=====================================================
"""

import json
import os
from datetime import datetime

# ==========================================
# FILE PATHS & CONSTANTS
# ==========================================

DATA_DIR = "data"
DATA_FILE = os.path.join(DATA_DIR, "expenses.json")

CATEGORIES = [
    "Food",
    "Transport",
    "Entertainment",
    "Shopping",
    "Health",
    "Education",
    "Other"
]

# ==========================================
# FILE STORAGE FUNCTIONS
# ==========================================


def load_expenses():
    """Load expense records from JSON file."""
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        return []


def save_expenses(expenses):
    """Save expense records to JSON file."""
    os.makedirs(DATA_DIR, exist_ok=True)
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(expenses, file, indent=4)


# ==========================================
# FORMATTING & DISPLAY HELPERS
# ==========================================


def print_separator(char="=", length=60):
    """Print horizontal divider line."""
    print(char * length)


def print_header(title):
    """Print decorated section header."""
    print_separator("=")
    print(f"  {title.upper()}")
    print_separator("=")


def display_expense_card(expense, index):
    """Display single expense in structured format."""
    print(f"\n  [{index}] {expense.get('description', 'No description')}")
    print(f"      Category : {expense.get('category', 'Uncategorized')}")
    print(f"      Amount   : Rs. {expense.get('amount', 0.0):.2f}")
    print(f"      Date     : {expense.get('date', 'N/A')}")


def display_all_expenses(expenses):
    """List all expenses formatted."""
    if not expenses:
        print("\n  [INFO] No expenses found.")
        return

    print_header("All Expense Records")
    for index, item in enumerate(expenses, start=1):
        display_expense_card(item, index)
        print_separator("-", 60)

    total = calculate_total(expenses)
    print(f"\n  Total Records : {len(expenses)}")
    print(f"  Total Spending: Rs. {total:.2f}")
    print_separator("=")


# ==========================================
# ANALYTICAL & CALCULATION FUNCTIONS
# ==========================================


def calculate_total(expenses):
    """Calculate the total sum of expenses."""
    return sum(item.get("amount", 0.0) for item in expenses)


def calculate_category_total(expenses, category):
    """Calculate the sum of expenses for a specific category."""
    return sum(item.get("amount", 0.0) for item in expenses if item.get("category") == category)


def find_highest_expense(expenses):
    """Return the expense dictionary with the largest amount."""
    if not expenses:
        return None
    return max(expenses, key=lambda x: x.get("amount", 0.0))


def find_lowest_expense(expenses):
    """Return the expense dictionary with the smallest amount."""
    if not expenses:
        return None
    return min(expenses, key=lambda x: x.get("amount", 0.0))


def calculate_average(expenses):
    """Calculate average expense amount."""
    if not expenses:
        return 0.0
    return calculate_total(expenses) / len(expenses)


# ==========================================
# CRUD OPERATIONS
# ==========================================


def add_expense(expenses):
    """Prompt user and record a new expense."""
    print_header("Add New Expense")

    description = input("  Enter expense description: ").strip()
    if not description:
        print("\n  [ERROR] Description cannot be empty.")
        return expenses

    try:
        amount = float(input("  Enter amount (Rs.): ").strip())
        if amount <= 0:
            print("\n  [ERROR] Amount must be greater than zero.")
            return expenses
    except ValueError:
        print("\n  [ERROR] Invalid amount. Please enter a valid numerical value.")
        return expenses

    print("\n  Select Category:")
    print_separator("-", 40)
    for idx, cat in enumerate(CATEGORIES, start=1):
        print(f"    {idx}. {cat}")
    print_separator("-", 40)

    try:
        cat_choice = int(input(f"  Select category (1-{len(CATEGORIES)}): ").strip())
        if 1 <= cat_choice <= len(CATEGORIES):
            category = CATEGORIES[cat_choice - 1]
        else:
            print("\n  [ERROR] Invalid category number.")
            return expenses
    except ValueError:
        print("\n  [ERROR] Please enter a valid number.")
        return expenses

    custom_date = input("  Enter date (YYYY-MM-DD) or press Enter for today: ").strip()
    if custom_date:
        try:
            valid_date = datetime.strptime(custom_date, "%Y-%m-%d")
            date_str = valid_date.strftime("%Y-%m-%d")
        except ValueError:
            print("\n  [WARNING] Invalid format. Defaulting to current date.")
            date_str = datetime.now().strftime("%Y-%m-%d")
    else:
        date_str = datetime.now().strftime("%Y-%m-%d")

    new_id = (max([e.get("id", 0) for e in expenses], default=0) + 1) if expenses else 1

    record = {
        "id": new_id,
        "description": description,
        "amount": round(amount, 2),
        "category": category,
        "date": date_str
    }

    expenses.append(record)
    save_expenses(expenses)

    print("\n  [SUCCESS] Expense recorded successfully!")
    print(f"  ID         : {record['id']}")
    print(f"  Description: {record['description']}")
    print(f"  Category   : {record['category']}")
    print(f"  Amount     : Rs. {record['amount']:.2f}")
    print(f"  Date       : {record['date']}")
    return expenses


def view_by_category(expenses):
    """View expenses filtered by a chosen category."""
    print_header("Expenses by Category")

    print("\n  Select Category:")
    print_separator("-", 40)
    for idx, cat in enumerate(CATEGORIES, start=1):
        cat_total = calculate_category_total(expenses, cat)
        print(f"    {idx}. {cat:<15} (Rs. {cat_total:.2f})")
    print_separator("-", 40)

    try:
        choice = int(input(f"  Select category (1-{len(CATEGORIES)}): ").strip())
        if not (1 <= choice <= len(CATEGORIES)):
            print("\n  [ERROR] Invalid category selection.")
            return
        selected_cat = CATEGORIES[choice - 1]
    except ValueError:
        print("\n  [ERROR] Please enter a valid number.")
        return

    filtered = [e for e in expenses if e.get("category") == selected_cat]

    print_header(f"Category: {selected_cat}")
    if not filtered:
        print(f"\n  No expenses recorded under '{selected_cat}'.")
        return

    for idx, item in enumerate(filtered, start=1):
        display_expense_card(item, idx)
        print_separator("-", 60)

    subtotal = calculate_total(filtered)
    print(f"\n  Items in Category: {len(filtered)}")
    print(f"  Category Subtotal: Rs. {subtotal:.2f}")
    print_separator("=")


def search_expenses(expenses):
    """Search for expenses matching a keyword."""
    print_header("Search Expenses")
    query = input("  Enter keyword to search (description/category): ").strip().lower()

    if not query:
        print("\n  [ERROR] Search keyword cannot be empty.")
        return

    matches = [
        e for e in expenses
        if query in e.get("description", "").lower() or query in e.get("category", "").lower()
    ]

    print_header(f"Search Results for '{query}'")
    if not matches:
        print(f"\n  No records found matching '{query}'.")
        return

    for idx, item in enumerate(matches, start=1):
        display_expense_card(item, idx)
        print_separator("-", 60)

    matched_total = calculate_total(matches)
    print(f"\n  Found: {len(matches)} record(s)")
    print(f"  Matching Sum: Rs. {matched_total:.2f}")
    print_separator("=")


def delete_expense(expenses):
    """Delete an expense record by its display number or ID."""
    if not expenses:
        print("\n  [INFO] No expenses available to delete.")
        return expenses

    display_all_expenses(expenses)

    try:
        item_num = int(input("\n  Enter record number [index] to delete: ").strip())
        if not (1 <= item_num <= len(expenses)):
            print("\n  [ERROR] Invalid record index.")
            return expenses
    except ValueError:
        print("\n  [ERROR] Please enter a valid number.")
        return expenses

    removed = expenses.pop(item_num - 1)
    save_expenses(expenses)

    print(f"\n  [DELETED] Successfully removed: '{removed.get('description')}' (Rs. {removed.get('amount', 0):.2f})")
    return expenses


def show_summary_report(expenses):
    """Generate and display analytical summary report."""
    print_header("Comprehensive Expense Summary")

    if not expenses:
        print("\n  [INFO] No expense data available to summarize.")
        return

    total = calculate_total(expenses)
    average = calculate_average(expenses)
    highest = find_highest_expense(expenses)
    lowest = find_lowest_expense(expenses)

    print(f"\n  Total Records   : {len(expenses)}")
    print(f"  Total Spend     : Rs. {total:.2f}")
    print(f"  Average Expense : Rs. {average:.2f}")

    if highest:
        print(f"\n  Highest Single Expense:")
        print(f"    - {highest.get('description')} : Rs. {highest.get('amount', 0):.2f} [{highest.get('category')}] on {highest.get('date')}")

    if lowest:
        print(f"\n  Lowest Single Expense:")
        print(f"    - {lowest.get('description')} : Rs. {lowest.get('amount', 0):.2f} [{lowest.get('category')}] on {lowest.get('date')}")

    print_separator("-", 60)
    print("  CATEGORY-WISE BREAKDOWN")
    print_separator("-", 60)

    for cat in CATEGORIES:
        cat_total = calculate_category_total(expenses, cat)
        if cat_total > 0:
            count = sum(1 for e in expenses if e.get("category") == cat)
            percentage = (cat_total / total) * 100 if total > 0 else 0
            print(f"  {cat:<15} : Rs. {cat_total:>8.2f} ({percentage:5.1f}%) | {count} item(s)")

    print_separator("=")


# ==========================================
# MAIN INTERACTIVE MENU
# ==========================================


def display_menu():
    """Print the interactive main menu."""
    print_separator("=")
    print("         EXPENSE TRACKER - MAIN MENU")
    print_separator("=")
    print("  1. Add New Expense")
    print("  2. View All Expenses")
    print("  3. Filter Expenses by Category")
    print("  4. Search Expenses by Keyword")
    print("  5. Generate Analytics & Summary Report")
    print("  6. Delete an Expense")
    print("  7. Exit")
    print_separator("=")


def main():
    """Application entrypoint and control loop."""
    print_separator("=")
    print("  WELCOME TO EXPENSE TRACKER CLI")
    print("  Module 2: Python Mini Project")
    print("  Author: Nandakishor Kalagarla (AI & ML)")
    print_separator("=")

    expenses = load_expenses()
    print(f"\n  [Loaded] {len(expenses)} expense record(s) from {DATA_FILE}.\n")

    while True:
        display_menu()
        choice = input("  Select an option (1-7): ").strip()

        if choice == "1":
            expenses = add_expense(expenses)
        elif choice == "2":
            display_all_expenses(expenses)
        elif choice == "3":
            view_by_category(expenses)
        elif choice == "4":
            search_expenses(expenses)
        elif choice == "5":
            show_summary_report(expenses)
        elif choice == "6":
            expenses = delete_expense(expenses)
        elif choice == "7":
            print_separator("=")
            print("  Thank you for using Expense Tracker!")
            print("  Have a great day!")
            print_separator("=")
            break
        else:
            print("\n  [ERROR] Invalid option selected. Please choose between 1 and 7.")

        input("\n  Press [Enter] to return to menu...")
        print("\n")


if __name__ == "__main__":
    main()
