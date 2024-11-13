import json
from datetime import datetime

# List to hold all tasks
tasks = []

# Function to add a new task
def add_task(description, deadline, priority):
    """
    Add a new task to the list.

    Args:
        description (str): Task description
        deadline (str): Task deadline in YYYY-MM-DD format
        priority (str): Task priority (high, medium, low)
    """
    task = {
        "description": description,
        "deadline": deadline,
        "priority": priority,
        "completed": False  # Initially, the task is not completed
    }
    tasks.append(task)
    print("Task added successfully!")

# Function to mark a task as complete
def mark_as_complete(task_index):
    """
    Mark a task as complete.

    Args:
        task_index (int): Index of the task to mark as complete
    """
    if 0 <= task_index < len(tasks):
        tasks[task_index]["completed"] = True
        print("Task marked as complete.")
    else:
        print("Invalid task number.")

# Function to view all tasks, sorted by a specified criterion
def view_tasks(sort_by="priority"):
    """
    View all tasks, sorted by a specified criterion.

    Args:
        sort_by (str): Criterion to sort by (priority or deadline)
    """
    if sort_by == "priority":
        sorted_tasks = sorted(tasks, key=lambda x: x["priority"])
    else:
        sorted_tasks = sorted(tasks, key=lambda x: datetime.strptime(x["deadline"], '%Y-%m-%d'))

    # Display each task with its status
    for index, task in enumerate(sorted_tasks):
        status = "✔️" if task["completed"] else "❌"
        print(
            f"{index + 1}. [{status}] {task['description']} (Deadline: {task['deadline']}, Priority: {task['priority']})")

# Function to search for tasks by keyword
def search_tasks(keyword):
    """
    Search for tasks by keyword.

    Args:
        keyword (str): Keyword to search for
    """
    found_tasks = [task for task in tasks if keyword.lower() in task["description"].lower()]
    if found_tasks:
        for task in found_tasks:
            status = "✔️" if task["completed"] else "❌"
            print(f"[{status}] {task['description']} (Deadline: {task['deadline']}, Priority: {task['priority']})")
    else:
        print("No tasks found with that keyword.")

# Function to generate and display statistics about tasks
def generate_statistics():
    """
    Generate and display statistics about tasks.
    """
    total_tasks = len(tasks)
    completed_tasks = sum(1 for task in tasks if task["completed"])
    pending_tasks = total_tasks - completed_tasks

    print(f"Total tasks: {total_tasks}")
    print(f"Completed tasks: {completed_tasks}")
    print(f"Pending tasks: {pending_tasks}")

# Function to export tasks to a JSON file
def export_data(filename):
    """
    Export tasks to a JSON file.

    Args:
        filename (str): Filename to export tasks to
    """
    with open(filename, 'w') as file:
        json.dump(tasks, file)
    print(f"Tasks exported to {filename}.")

# Main function to run the task manager
def main():
    while True:
        command = input("\nChoose an option: add, complete, view, search, stats, export, exit: ").strip().lower()

        if command == "add":
            desc = input("Task description: ")
            deadline = input("Deadline (YYYY-MM-DD): ")
            priority = input("Priority (high, medium, low): ")
            add_task(desc, deadline, priority)
        elif command == "complete":
            task_index = int(input("Task number to complete: ")) - 1
            mark_as_complete(task_index)
        elif command == "view":
            sort_by = input("Sort by (priority/deadline): ").strip().lower()
            view_tasks(sort_by)
        elif command == "search":
            keyword = input("Enter keyword to search: ")
            search_tasks(keyword)
        elif command == "stats":
            generate_statistics()
        elif command == "export":
            filename = input("Filename to export tasks (e.g., tasks.json): ")
            export_data(filename)
        elif command == "exit":
            print("Exiting Task Manager. Goodbye!")
            break
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()