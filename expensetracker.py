# expenses.py - Handles expense-related functions

def add_expense(expenses, amount, category, date):
    """
    Adds a new expense to the expenses list.
    
    Parameters:
    expenses (list): The list of existing expenses.
    amount (float): The amount spent.
    category (str): The category of the expense.
    date (str): The date of the expense in YYYY-MM-DD format.
    """
    expenses.append({"amount": amount, "category": category, "date": date})

def total_expenses(expenses):
    """
    Calculates the total amount spent.

    Parameters:
    expenses (list): The list of expenses.

    Returns:
    float: Total sum of all expenses.
    """
    return sum(expense["amount"] for expense in expenses)

def expenses_by_category(expenses):
    """
    Groups expenses by category and calculates the total spent in each.

    Parameters:
    expenses (list): The list of expenses.

    Returns:
    dict: A dictionary where keys are categories and values are total amounts spent.
    """
    categories = {}
    for expense in expenses:
        category = expense["category"]
        categories[category] = categories.get(category, 0) + expense["amount"]
    return categories

def filter_by_category(expenses, category):
    """
    Filters expenses based on the given category.

    Parameters:
    expenses (list): The list of expenses.
    category (str): The category to filter.

    Returns:
    list: A list of expenses matching the category.
    """
    return [expense for expense in expenses if expense["category"] == category]

def filter_by_date_range(expenses, start_date, end_date):
    """
    Filters expenses that fall within a given date range.

    Parameters:
    expenses (list): The list of expenses.
    start_date (str): The start date in YYYY-MM-DD format.
    end_date (str): The end date in YYYY-MM-DD format.

    Returns:
    list: A list of expenses that fall within the specified date range.
    """
    return [expense for expense in expenses if start_date <= expense["date"] <= end_date]
