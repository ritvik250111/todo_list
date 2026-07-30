"""
==========================================
        TO-DO LIST APPLICATION
==========================================

A simple command-line To-Do List application.

Features:
1. Add Tasks
2. View Tasks
3. Delete Tasks
4. Quit

Tasks are stored in a Python list.
"""

# List to store tasks
tasks = []


def show_menu():
    """Display the main menu."""
    print("\n==============================")
    print("       TO-DO LIST MENU")
    print("==============================")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Quit")


def add_task():
    """Add a new task to the list."""
    task = input("Enter your task: ").strip()

    if task == "":
        print("Task cannot be empty.")
    else:
        tasks.append(task)
        print(f'"{task}" has been added successfully.')


def view_tasks():
    """Display all tasks."""

    try:
        if len(tasks) == 0:
            raise ValueError("No tasks available.")

    except ValueError as error:
        print(error)

    else:
        print("\nYour Tasks:")
        print("-" * 30)

        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

    finally:
        print("-" * 30)


def delete_task():
    """Delete a task from the list."""

    try:
        if len(tasks) == 0:
            raise ValueError("There are no tasks to delete.")

        view_tasks()

        choice = int(input("Enter the task number to delete: "))

        if choice < 1 or choice > len(tasks):
            raise IndexError

    except ValueError:
        print("Please enter a valid number.")

    except IndexError:
        print("Task does not exist.")

    else:
        removed_task = tasks.pop(choice - 1)
        print(f'"{removed_task}" has been deleted.')

    finally:
        print("Returning to main menu...")


def main():
    """Run the application."""

    print("=" * 40)
    print(" Welcome to the Python To-Do List ")
    print("=" * 40)

    while True:

        show_menu()

        try:
            option = input("Choose an option (1-4): ").strip()

            if option == "1":
                add_task()

            elif option == "2":
                view_tasks()

            elif option == "3":
                delete_task()

            elif option == "4":
                print("\nThank you for using the To-Do List App.")
                print("Goodbye!")
                break

            else:
                raise ValueError

        except ValueError:
            print("Invalid menu option. Please choose between 1 and 4.")

        finally:
            print()


# Run the program
if __name__ == "__main__":
    main()