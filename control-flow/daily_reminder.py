# daily_reminder.py

# Prompt user for task details
task = input("Enter your task: ")

# Prompt user for priority level and validate input
while True:
    priority = input("Priority (high/medium/low): ").strip().lower()
    if priority in ["high", "medium", "low"]:
        break
    else:
        print("Invalid input. Please enter 'high', 'medium', or 'low'.")

# Prompt user for time-bound status and validate input
while True:
    time_bound = input("Is it time-bound? (yes/no): ").strip().lower()
    if time_bound in ["yes", "no"]:
        break
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")

# Construct reminder based on priority and time-bound status using match case
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task."
    case "medium":
        reminder = f"'{task}' is a medium priority task."
    case "low":
        reminder = f"'{task}' is a low priority task."
    case _:
        reminder = "Invalid priority level entered."

# Append time-bound message if necessary
if time_bound == "yes":
    reminder += " That requires immediate attention today!"

# Print the reminder message
print("Reminder:", reminder)
