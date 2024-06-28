# daily_reminder.py

# Prompt user for task details
task = input("Enter the task description: ")

# Prompt user for priority level and validate input
while True:
    priority = input("Enter the priority level (high, medium, low): ").strip().lower()
    if priority in ["high", "medium", "low"]:
        break
    else:
        print("Invalid input. Please enter 'high', 'medium', or 'low'.")

# Prompt user for time-bound status and validate input
while True:
    time_bound = input("Is the task time-bound? (yes or no): ").strip().lower()
    if time_bound in ["yes", "no"]:
        break
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")

# Construct reminder based on priority and time-bound status
reminder = f"Task: {task}\nPriority: {priority.capitalize()}"
if time_bound == "yes":
    reminder += "\nThis task requires immediate attention today!"

# Print the reminder message
print(reminder)
