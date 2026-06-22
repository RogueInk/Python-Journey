# 3. Expense Tracker
# Features: Add expenses, View expenses, Calculate total spending, Find highest expense category
# Concepts: Nested dictionaries, Loops, Functions
# Challenge: Generate monthly reports

# Defining Variables
expenses = {}

# This function adds an expense to the expenses dictionary.
def AddExpense(category, amount):
    if category in expenses:
        expenses[category] += amount
    else:
        expenses[category] = amount
        print(f"Added {amount} to {category}. Total in {category}: {expenses[category]}")

# This function displays all expenses in the expenses dictionary.
def ViewExpenses():
    if not expenses:
        print("No expenses recorded yet.")
    else:
        print("Expenses by category:")
        for category, amount in expenses.items():
            print(f"{category}: {amount}")

# This function calculates the total spending across all categories.
def CalculateTotalSpending():
    total = sum(expenses.values())
    print(f"Total spending: {total}")
    return total

# This function finds the category with the highest expense.
def FindHighestExpenseCategory():
    if not expenses:
        print("No expenses recorded yet.")
        return None
    highest_category = max(expenses, key=expenses.get)
    print(f"Highest expense category: {highest_category} with amount {expenses[highest_category]}")
    return highest_category

# Main Program Loop
while True:
    print("\nExpense Tracker")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Calculate Total Spending")
    print("4. Find Highest Expense Category")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        category = input("Enter expense category: ")
        amount = float(input("Enter expense amount: "))
        AddExpense(category, amount)

    elif choice == "2":
        ViewExpenses()

    elif choice == "3":
        CalculateTotalSpending()

    elif choice == "4":
        FindHighestExpenseCategory()

    elif choice == "5":
        print("Exiting Expense Tracker. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")


