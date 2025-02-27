# utils.py - Contains helper functions for input validation

def get_float_input(prompt):
    """
    Ensures the user inputs a valid floating-point number.

    Parameters:
    prompt (str): The message to display for user input.

    Returns:
    float: A valid floating-point number.
    """
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_date_input(prompt):
    """
    Ensures the user inputs a date in YYYY-MM-DD format.

    Parameters:
    prompt (str): The message to display for user input.

    Returns:
    str: A valid date string in YYYY-MM-DD format.
    """
    while True:
        date = input(prompt)
        if len(date) == 10 and date[4] == '-' and date[7] == '-':  # Basic format check
            return date
        print("Invalid date format. Please use YYYY-MM-DD.")
