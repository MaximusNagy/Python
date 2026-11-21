from datetime import datetime
import calendar  # Import calendar to find days in a month

print("\nWelcome to the age calculator!")

try:
    while True:
        # Get current date *inside* the loop in case the program runs for a long time
        today = datetime.now()
        current_year = today.year
        current_month = today.month
        current_day = today.day

        # --- Input and Validation ---
        year = int(input("Enter your year of birth: "))
        month = int(input("Enter your birth month (1-12): "))
        day = int(input("Enter your birth day: "))

        # Basic validation
        if month < 1 or month > 12:
            print("Invalid month! Please enter a value between 1 and 12.")
            continue
        
        # Check for valid day in that specific month
        days_in_birth_month = calendar.monthrange(year, month)[1]
        if day < 1 or day > days_in_birth_month:
            print(f"Invalid day! That month only has {days_in_birth_month} days.")
            continue

        # Check if birth date is in the future
        birth_date = datetime(year, month, day)
        if birth_date > today:
            print("Birth date cannot be in the future!")
            continue

        # --- Correct Age Calculation ---

        # Start with simple subtraction
        age_year = current_year - year
        age_month = current_month - month
        age_day = current_day - day

        # 1. Adjust for negative days (borrow from month)
        if age_day < 0:
            # Borrow one month
            age_month -= 1
            # Find days in the *previous* month (relative to current_month)
            # (current_month - 1) is the previous month. If it's 0, it means December of last year.
            prev_month = current_month - 1
            prev_year = current_year
            if prev_month == 0:
                prev_month = 12
                prev_year -= 1
            
            # Get the number of days in that previous month
            days_in_prev_month = calendar.monthrange(prev_year, prev_month)[1]
            
            # Add those days to the negative day count
            age_day += days_in_prev_month

        # 2. Adjust for negative months (borrow from year)
        if age_month < 0:
            # Borrow one year
            age_year -= 1
            # Add 12 months
            age_month += 12

        # --- Display Result ---
        result = f"Your age is: {age_year} years, {age_month} months, {age_day} days."
        print(result)
        
        out = input("Do you want to exit? (press 1 to exit, anything else to continue): ")
        if out == "1":
            break
        
except ValueError:
    print("Invalid input! Please enter a numeric value for date parts.")