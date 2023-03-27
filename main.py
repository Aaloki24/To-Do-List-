# Define an empty list to store tasks
tasks = []

# Define a function to add a task to the list
def add_task(task):
    tasks.append(task)
    print(f"Added task '{task}' to the list.")

# Define a function to remove a task from the list
def remove_task(task):
    try:
        tasks.remove(task)
        print(f"Removed task '{task}' from the list.")
    except ValueError:
        print(f"Task '{task}' is not in the list.")

# Define a function to display all tasks in the list
def display_tasks():
    if not tasks:
        print("There are no tasks in the list.")
    else:
        print("Tasks in the list:")
        for task in tasks:
            print(f"- {task}")

# Start the program loop
while True:
    # Display the options menu
    print("\nOptions:")
    print("1. Add a task")
    print("2. Remove a task")
    print("3. Display all tasks")
    print("4. Exit")
    
    # Get the user's choice
    choice = input("Enter your choice (1-4): ")
    
    # Perform the selected action
    if choice == "1":
        task = input("Enter the task to add: ")
        add_task(task)
    elif choice == "2":
        task = input("Enter the task to remove: ")
        remove_task(task)
    elif choice == "3":
        display_tasks()
    elif choice == "4":
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
