tasks = []

def show_tasks():
    if not tasks:
        print("\nNo tasks available.")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added successfully!")

def update_task():
    show_tasks()
    if tasks:
        num = int(input("Enter task number to update: "))
        if 1 <= num <= len(tasks):
            new_task = input("Enter new task: ")
            tasks[num - 1] = new_task
            print("Task updated successfully!")
        else:
            print("Invalid task number.")

def delete_task():
    show_tasks()
    if tasks:
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            print(f"Task '{removed}' deleted successfully!")
        else:
            print("Invalid task number.")

while True:
    print("\n--- TO-DO LIST MENU ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        show_tasks()
    elif choice == "3":
        update_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Please try again.")