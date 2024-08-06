import csv
from datetime import datetime

# Constants
DATA_FILE = 'expenses.csv'
CATEGORIES = ['Food', 'Transportation', 'Entertainment', 'Others']

# Function to input expense
def input_expense():
    try:
        amount = float(input("Enter amount: "))
        description = input("Enter description: ")
        category = input(f"Enter category ({', '.join(CATEGORIES)}): ")
        if category not in CATEGORIES:
            raise ValueError("Invalid category")
        date = datetime.now().strftime("%Y-%m-%d")
        return {'amount': amount, 'description': description, 'category': category, 'date': date}
    except ValueError as e:
        print(f"Error: {e}")
        return None

# Function to save expense
def save_expense(expense):
    with open(DATA_FILE, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=expense.keys())
        if file.tell() == 0:
            writer.writeheader()
        writer.writerow(expense)

# Function to read expenses
def read_expenses():
    expenses = []
    try:
        with open(DATA_FILE, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                expenses.append(row)
    except FileNotFoundError:
        print("No expenses found. Start adding your expenses!")
    return expenses

# Function to analyze expenses
def analyze_expenses(expenses):
    total_expense = sum(float(expense['amount']) for expense in expenses)
    category_expense = {category: 0 for category in CATEGORIES}
    for expense in expenses:
        category_expense[expense['category']] += float(expense['amount'])
    return total_expense, category_expense

# Main function
def main():
    while True:
        print("\n1. Add Expense")
        print("2. View Summary")
        print("3. Exit")
        choice = input("Enter choice: ")
        
        if choice == '1':
            expense = input_expense()
            if expense:
                save_expense(expense)
                print("Expense added successfully!")
        elif choice == '2':
            expenses = read_expenses()
            total, category_expense = analyze_expenses(expenses)
            print(f"\nTotal Expense: {total}")
            for category, amount in category_expense.items():
                print(f"{category}: {amount}")
        elif choice == '3':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
