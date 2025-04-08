# Function to display tasks
def view_tasks(tasks):
    if tasks:
        print("\nYour To-Do List:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")
    else:
        print("\nYour To-Do list is empty.")


# Function to add a task
def add_task(tasks):
    task = input("\nEnter a task: ")
    tasks.append(task)


# Function to remove a task
def remove_task(tasks):
    view_tasks(tasks)
    try:
        task_number = int(input("\nEnter task number to remove: "))
        if 1 <= task_number <= len(tasks):
            tasks.pop(task_number - 1)
            print("Task removed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


# Main function
def main():
    tasks = []
    while True:
        print("\n1. View tasks")
        print("2. Add a task")
        print("3. Remove a task")
        print("4. Exit")

        choice = input("\nEnter choice (1/2/3/4): ")

        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")


# Run the application
if __name__ == "__main__":
    main()
