# Create an empty list to store tasks
tasks = []

# Function to add a task to the list
def add_task(task):
    tasks.append(task)
    print(f'Task "{task}" added.')

# Function to list all tasks
def list_tasks():
    if not tasks:
        print('No tasks in the to-do list.')
    else:
        print('Tasks in the to-do list:')
        for i, task in enumerate(tasks, 1):
            print(f'{i}. {task}')

# Function to remove a task by its index
def remove_task(index):
    if 1 <= index <= len(tasks):
        removed_task = tasks.pop(index - 1)
        print(f'Task "{removed_task}" removed.')
    else:
        print('Invalid task index.')

# Main loop
while True:
    print("\nOptions:")
    print("1. Add task")
    print("2. List tasks")
    print("3. Remove task")
    print("4. Quit")
    
    choice = input("Enter your choice (1/2/3/4): ")
    
    if choice == '1':
        task = input("Enter a new task: ")
        add_task(task)
    elif choice == '2':
        list_tasks()
    elif choice == '3':
        index = int(input("Enter the index of the task to remove: "))
        remove_task(index)
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please choose 1, 2, 3, or 4.")
