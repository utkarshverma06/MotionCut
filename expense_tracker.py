import json

class Expense:
    def __init__(self, amount, description, category, date):
        self.amount = amount
        self.description = description
        self.category = category
        self.date = date

    def to_dict(self):
        return {
            "amount": self.amount,
            "description": self.description,
            "category": self.category,
            "date": self.date
        }

def load_expenses():
    try:
        with open('expenses.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_expenses(expenses):
    with open('expenses.json', 'w') as file:
        json.dump(expenses, file, indent=4)

def enter_expense(expenses):
    try:
        amount = float(input("Enter the expense amount: "))
    except ValueError:
        print("Please enter a valid number for the amount.")
        return
    
    description = input("Enter a brief description: ")
    category = input("Enter the category (e.g., Food, Transportation, Entertainment): ")
    date = input("Enter the date (YYYY-MM-DD): ")
    
    expense = Expense(amount, description, category, date)
    expenses.append(expense.to_dict())
    print("Expense added successfully!")

def view_monthly_summary(expenses):
    month = input("Enter the month (YYYY-MM): ")
    total = 0
    for expense in expenses:
        if expense['date'].startswith(month):
            total += expense['amount']
    print(f"Total expenses for {month}: ${total:.2f}")

def view_category_summary(expenses):
    categories = set(expense['category'] for expense in expenses)
    for category in categories:
        total = sum(expense['amount'] for expense in expenses if expense['category'] == category)
        print(f"Total spent on {category}: ${total:.2f}")

def main():
    expenses = load_expenses()
    while True:
        print("\n--- Expense Tracker ---")
        print("1. Enter Expense")
        print("2. View Monthly Summary")
        print("3. View Category Summary")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            enter_expense(expenses)
        elif choice == "2":
            view_monthly_summary(expenses)
        elif choice == "3":
            view_category_summary(expenses)
        elif choice == "4":
            save_expenses(expenses)
            print("Data saved. Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
