from datetime import datetime

def get_date(prompt):
    """
    Continuously prompts the user for a date string until a valid date is entered.

    Args:
        prompt(str): The prompt message to display to the user.

    Returns:
        datetime: A valid datetime object parsed from user input.
    """
    while True:
        user_input = input(prompt)
        try:
            return datetime.strptime(user_input, "%Y-%m-%d")
        except ValueError:
            print("Oops! Please enter the date in YYYY-MM-DD format.")

def main():
    """
    Main function to interact with the user, take two dates as input,
    and print the number of days between them.
    """
    print("Let's find out how many days are between two dates.")
    
    first_date = get_date("Enter the first date (YYYY-MM-DD): ")
    second_date = get_date("Enter the second date (YYYY-MM-DD): ")
    
    days_diff = abs((second_date - first_date).days)
    print(f"There are {days_diff} days between those two dates.")

if __name__ == "__main__":
    main()
