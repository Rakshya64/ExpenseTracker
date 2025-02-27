# Expense Tracker

A simple command-line-based Expense Tracker program written in Python. It allows users to record expenses, categorize them, and filter them by date or category.

## Features
- Add new expenses (amount, category, date)
- View total expenses
- View expenses grouped by category
- Filter expenses by category
- Filter expenses by date range
- Simple and interactive CLI menu

## Installation

### Prerequisites
Ensure you have Python installed on your system. You can check by running:
```sh
python --version
```
If Python is not installed, download it from [python.org](https://www.python.org/downloads/).

### Clone the Repository
```sh
git clone https://github.com/Rakshya64/ExpenseTracker.git
cd ExpenseTracker

cd expense-tracker
```

### Run the Program
```sh
python main.py
```

## Usage
When you run `main.py`, you will see a menu:
```
Expense Tracker Menu:
1. Add Expense
2. View Total Expenses
3. View Expenses by Category
4. Filter Expenses by Category
5. Filter Expenses by Date Range
6. Exit
```
### Adding an Expense
1. Enter the amount spent.
2. Enter the category (e.g., Food, Transport, Entertainment).
3. Enter the date in `YYYY-MM-DD` format.

### Viewing Total Expenses
Select option `2` to see the total amount spent.

### Viewing Expenses by Category
Select option `3` to see a breakdown of expenses by category.

### Filtering by Category
Select option `4`, then enter a category to see only expenses in that category.

### Filtering by Date Range
Select option `5`, then enter a start and end date in `YYYY-MM-DD` format.

## Folder Structure
```
expense-tracker/
│── main.py           # Main program file
│── expensetracker.py # Expense management functions
│── utils.py    # Utility functions (input validation)
│── README.md         # Documentation
```

## Future Enhancements
- Store expenses in a file (JSON/CSV) to persist data
- Add a graphical user interface (GUI)
- Generate reports and statistics


