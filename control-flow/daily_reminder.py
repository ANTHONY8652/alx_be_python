# daily_reminder.py

# Prompt the user for task details
task = input("Enter the task description: ")
priority = input("Enter the priority level (high, medium, low): ")
time_bound = input("Is the task time-bound? (yes or no): ")

# Match Case statement to react based on task priority
match priority:
    case "high":
        reminder = f"Task: {task}\nPriority: {priority.capitalize()}"
        if time_bound.lower() == "yes":
            reminder += "\nThis task requires immediate attention today!"
        print(reminder)
    case "medium":
        reminder = f"Task: {task}\nPriority: {priority.capitalize()}"
        if time_bound.lower() == "yes":
            reminder += "\nThis task requires immediate attention today!"
        print(reminder)
    case "low":
        reminder = f"Task: {task}\nPriority: {priority.capitalize()}"
        if time_bound.lower() == "yes":
            reminder += "\nThis task requires immediate attention today!"
        print(reminder)
    case _:
        print("Invalid priority level entered.")

