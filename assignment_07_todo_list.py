# =============================================================================
def display_menu():
    """Displays the main application menu."""
    print("\n============================")
    print("        TO-DO LIST MENU     ")
    print("============================")
    print("1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Quit")


def add_task(tasks):
    """Prompts user for a task description and adds it to the list."""
    task = input("Enter task: ").strip()
    if task:
        tasks.append(task)
        print(f'Task added: "{task}"')
    else:
        print("Error: Task description cannot be empty.")


def view_tasks(tasks):
    """Displays all current tasks with 1-based indexing."""
    if not tasks:
        print("Your to-do list is empty!")
        return

    print("\nYour Tasks:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")


def delete_task(tasks):
    """Prompts for a task number and removes it from the list."""
    if not tasks:
        print("No tasks available to delete.")
        return

    view_tasks(tasks)
    user_input = input("Enter task number to delete: ").strip()

    if not user_input.isdigit():
        print("Error: Please enter a valid number.")
        return

    task_number = int(user_input)

    # Validate that the number corresponds to an existing item
    if 1 <= task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        print(f'Task "{removed_task}" has been removed.')
    else:
        print("Error: Invalid task number.")


def main():
    """Main program loop."""
    tasks = []

    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please select an option between 1 and 4.")


if __name__ == "__main__":
    main()