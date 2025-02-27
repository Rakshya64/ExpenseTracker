from expensetracker import add_expense, total_expenses, expenses_by_category, filter_by_category, filter_by_date_range
from utils import get_float_input, get_date_input

def display_menu():
    """
    Displays the menu options for the user.
    """
    print("\nExpense Tracker Menu:")
    print("1. Add Expense")
    print("2. View Total Expenses")
    print("3. View Expenses by Category")
    print("4. Filter Expenses by Category")
    print("5. Filter Expenses by Date Range")
    print("6. Exit")

def main():
    """
    Main function that handles user input and program execution.
    """
    expenses = []  # Stores expense data

    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            # Add a new expense
            print("\nAdd a New Expense")
            amount = get_float_input("Enter the amount spent: $")
            category = input("Enter the category (e.g., Food, Transport, Entertainment): ")
            date = get_date_input("Enter the date (YYYY-MM-DD): ")
            add_expense(expenses, amount, category, date)
            print(f"Expense of ${amount:.2f} in '{category}' on {date} added successfully!")

        elif choice == "2":
            # Display total expenses
            total = total_expenses(expenses)
            print(f"\nTotal Expenses: ${total:.2f}")

        elif choice == "3":
            # Display expenses grouped by category
            categories = expenses_by_category(expenses)
            print("\nExpenses by Category:")
            for category, amount in categories.items():
                print(f"{category}: ${amount:.2f}")

        elif choice == "4":
            # Filter expenses by category
            category = input("\nEnter the category to filter (e.g., Food, Transport): ")
            filtered = filter_by_category(expenses, category)
            if filtered:
                print(f"\nExpenses in '{category}':")
                for expense in filtered:
                    print(f"Amount: ${expense['amount']:.2f}, Date: {expense['date']}")
            else:
                print(f"No expenses found in '{category}'.")

        elif choice == "5":
            # Filter expenses by date range
            print("\nFilter Expenses by Date Range")
            start_date = get_date_input("Enter the start date (YYYY-MM-DD): ")
            end_date = get_date_input("Enter the end date (YYYY-MM-DD): ")
            filtered = filter_by_date_range(expenses, start_date, end_date)
            if filtered:
                print(f"\nExpenses from {start_date} to {end_date}:")
                for expense in filtered:
                    print(f"Amount: ${expense['amount']:.2f}, Category: {expense['category']}, Date: {expense['date']}")
            else:
                print(f"No expenses found between {start_date} and {end_date}.")

        elif choice == "6":
            # Exit the program
            print("\nExiting program. Goodbye!")
            break

        else:
            # Handle invalid input
            print("\nInvalid choice. Please enter a number between 1 and 6.")

# Run the program
if __name__ == "__main__":
    main()
