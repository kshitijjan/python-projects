import json
from datetime import datetime

# In-memory storage for expenses
expenses = []

def save_expenses_to_file():
    """
    Save the current list of expenses to a JSON file.
    """
    with open('expenses.json', 'w') as file:
        json.dump(expenses, file)

def load_expenses_from_file():
    """
    Load the list of expenses from a JSON file into memory.
    """
    global expenses
    try:
        with open('expenses.json', 'r') as file:
            expenses = json.load(file)
    except FileNotFoundError:
        expenses = []

def get_expense_input():
    """
    Prompt the user to input expense details and return them as a dictionary.
    Returns None if input is invalid.
    """
    try:
        # Prompt user for expense amount, description, and category
        amount = float(input("Enter the amount: "))
        description = input("Enter a brief description: ")
        category = input("Enter the category: ")
        # Use the current date for the expense entry
        date = datetime.now().strftime('%Y-%m-%d')
        # Return the expense details as a dictionary
        return {"date": date, "amount": amount, "description": description, "category": category}
    except ValueError:
        # Handle invalid amount input
        print("Invalid input. Please enter numeric values for the amount.")
        return None

def add_expense(expense):
    """
    Add a new expense to the list and save the updated list to a file.
    """
    expenses.append(expense)
    save_expenses_to_file()

def monthly_summary():
    """
    Generate a summary of expenses for each month.
    Returns a dictionary with months as keys and total amounts as values.
    """
    summary = {}
    for expense in expenses:
        date = expense["date"]
        amount = expense["amount"]
        month = date[:7]  # Extract YYYY-MM from the date
        if month not in summary:
            summary[month] = 0
        summary[month] += amount
    return summary

def category_summary():
    """
    Generate a summary of expenses for each category.
    Returns a dictionary with categories as keys and total amounts as values.
    """
    summary = {}
    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]
        if category not in summary:
            summary[category] = 0
        summary[category] += amount
    return summary

def print_summary(summary, summary_type):
    """
    Print the expense summary in a readable format.
    """
    print(f"{summary_type} Summary")
    for key, value in summary.items():
        print(f"{key}: Rs.{value:.2f}")

def main():
    """
    Main function to run the Expense Tracker application.
    """
    load_expenses_from_file()
    print("Welcome to the Expense Tracker")
    while True:
        # Display menu options
        print("1. Add Expense\n2. View Monthly Summary\n3. View Category Summary\n4. Exit")
        choice = input("Enter your choice: ").strip()
        if choice == '1':
            # Add a new expense
            expense = get_expense_input()
            if expense:
                add_expense(expense)
                print("Expense saved successfully!")
            else:
                print("Failed to save expense.")
        elif choice == '2':
            # Display monthly summary
            summary = monthly_summary()
            print_summary(summary, "Monthly")
        elif choice == '3':
            # Display category summary
            summary = category_summary()
            print_summary(summary, "Category")
        elif choice == '4':
            # Exit the application
            break
        else:
            # Handle invalid menu choice
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
