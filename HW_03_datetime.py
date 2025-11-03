from datetime import datetime

def get_days_from_today(date):   # Create a function that calculates amount of days
    try:
        input_date = datetime.strptime(date, "%Y-%m-%d").date()   # Convert input_date into datetime object 
        today = datetime.today().date()   # Get the current date
        diff_days = (today - input_date).days   # Calculate the difference between current date and set date
        return diff_days
    except ValueError:
        return "Incorrect format. Must be YYYY-MM-DD"

print(get_days_from_today("2025.10.31"))
print(get_days_from_today("2025-10-31"))
