from datetime import datetime

print("\nWelcome to the time remaining calculator!")

# Get the current date and time
current_date = datetime.now()

# Get user input for the target date
year = int(input("Enter the year: "))
month = int(input("Enter the month: "))
day = int(input("Enter the day: "))

# Create a datetime object for the target date
target_date = datetime(year, month, day)

# Calculate the difference between the current date and the target date
difference = target_date - current_date

# Extract remaining days, hours, and minutes
days_remaining = difference.days
hours_remaining = difference.seconds // 3600
minutes_remaining = (difference.seconds % 3600) // 60

if days_remaining >= 0:
    print(f"\nTime remaining until this date: {days_remaining} days, {hours_remaining} hours, and {minutes_remaining} minutes.")
else:
    print("\nThis date has already passed!")
