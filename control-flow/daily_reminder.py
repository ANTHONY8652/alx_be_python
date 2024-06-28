# daily_reminder.py

# Function to prompt user for input and validate responses
def prompt_for_input(prompt, valid_options=None):
    while True:
        user_input = input(prompt).strip().lower()
        if valid_options is None or user_input in valid_options:
            return user_input
        else:
            print("Invalid input. Please try again.")

# Prompt the user for task details
task = input("Enter the task description: ")

# Prompt and validate priority level
priority_options = ["high", "medium", "low"]
priority = prompt_for_input("Enter the priority level (high, medium, low): ", priority_options)

# Prompt and validate time-bound option
time_bound_options = ["yes", "no"]
time_bound = prompt_for_input("Is the task time-bound? (yes or no): ", time_bound_options)

# Match Case statement to react based on task priority
match priority:
    case "high":
        reminder = f"Task: {task}\nPriority: {priority.capitalize()}"
        if time_bound == "yes":
            reminder += "\nThis task requires immediate attention today!"
        print(reminder)
    case "medium":
        reminder = f"Task: {task}\nPriority: {priority.capitalize()}"
        if time_bound == "yes":
            reminder += "\nThis task requires immediate attention today!"
        print(reminder)
    case "low":
        reminder = f"Task: {task}\nPriority: {priority.capitalize()}"
        if time_bound == "yes":
            reminder += "\nThis task requires immediate attention today!"
        print(reminder)
    case _:
        print("Invalid priority level entered.")
