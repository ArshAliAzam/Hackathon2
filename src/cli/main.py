#!/usr/bin/env python3
"""
Main entry point for the Todo Console Application (Interactive Mode)
"""

import sys
import os
import time

# Add the src directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from src.services.task_manager import TaskManager

# 🎨 COLORS (no heavy libs)
COLORS = [
    "\033[91m",  # RED
    "\033[93m",  # YELLOW
    "\033[92m",  # GREEN
    "\033[96m",  # CYAN
    "\033[94m",  # BLUE
    "\033[95m",  # MAGENTA
]
RESET = "\033[0m"
BOLD = "\033[1m"


def rainbow_text(text, delay=0.004):
    for i, char in enumerate(text):
        print(COLORS[i % len(COLORS)] + char, end="", flush=True)
        time.sleep(delay)
    print(RESET)


def spinner(text="Processing", duration=1.2):
    frames = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
    end_time = time.time() + duration
    i = 0
    while time.time() < end_time:
        print(f"\r\033[96m{text} {frames[i % len(frames)]}\033[0m", end="", flush=True)
        time.sleep(0.1)
        i += 1
    print("\r" + " " * 40, end="\r")


def print_menu():
    print("\n")
    rainbow_text("████████╗ ██████╗ ██████╗  ██████╗ ")
    rainbow_text("╚══██╔══╝██╔═══██╗██╔══██╗██╔═══██╗")
    rainbow_text("   ██║   ██║   ██║██║  ██║██║   ██║")
    rainbow_text("   ██║   ██║   ██║██║  ██║██║   ██║")
    rainbow_text("   ██║   ╚██████╔╝██████╔╝╚██████╔╝")
    rainbow_text("   ╚═╝    ╚═════╝ ╚═════╝  ╚═════╝ ")

    print(BOLD + "\033[93m📝 TODO CONSOLE APPLICATION\033[0m\n")

    print("\033[92m1. ➕ Add task\033[0m")
    print("\033[96m2. 📃 List tasks\033[0m")
    print("\033[94m3. 📈 Update task status\033[0m")
    print("\033[95m4. 🙃 Update task details\033[0m")
    print("\033[91m5. 🗑️  Delete task\033[0m")
    print("\033[93m6. ❔ Exit\033[0m")
    print("\033[90m" + "-" * 50 + RESET)


def main():
    task_manager = TaskManager()

    while True:
        print_menu()
        choice = input("\033[97mSelect an option (1-6): \033[0m").strip()

        # ADD TASK
        if choice == "1":
            title = input("Enter task title: ").strip()
            description = input("Enter task description (optional): ").strip()
            description = description if description else None

            spinner("Adding task")
            task = task_manager.add_task(title, description)
            print(f"\033[92m✅ Task added with ID: {task.id}\033[0m")

        # LIST TASKS
        elif choice == "2":
            spinner("Fetching tasks")
            tasks = task_manager.list_tasks()
            if not tasks:
                print("\033[93m⚠️ No tasks found.\033[0m")
            else:
                print("\n\033[96mTask List:\033[0m")
                print("\033[90m" + "-" * 50 + RESET)
                for task in tasks:
                    status = "\033[92m✓\033[0m" if task.completed else "\033[91m○\033[0m"
                    desc = task.description or "No description"
                    print(f"{status} [{task.id}] {task.title}")
                    print(f"    \033[90mDescription:\033[0m {desc}")

        # UPDATE STATUS
        elif choice == "3":
            try:
                task_id = int(input("Enter task ID: "))
                status = input("Enter status (complete / incomplete): ").strip().lower()
                spinner("Updating status")
                task_manager.update_task_status(task_id, status == "complete")
                print("\033[92m✅ Task status updated.\033[0m")
            except ValueError as e:
                print(f"\033[91m❌ Error: {e}\033[0m")

        # UPDATE TASK
        elif choice == "4":
            try:
                task_id = int(input("Enter task ID: "))
                title = input("New title (leave empty to skip): ").strip()
                description = input("New description (leave empty to skip): ").strip()

                title = title if title else None
                description = description if description else None

                spinner("Updating task")
                task_manager.update_task_details(task_id, title, description)
                print("\033[92m✅ Task updated.\033[0m")
            except ValueError as e:
                print(f"\033[91m❌ Error: {e}\033[0m")

        # DELETE TASK
        elif choice == "5":
            try:
                task_id = int(input("Enter task ID to delete: "))
                spinner("Deleting task")
                task_manager.delete_task(task_id)
                print("\033[91m🗑️ Task deleted.\033[0m")
            except ValueError as e:
                print(f"\033[91m❌ Error: {e}\033[0m")

        # EXIT
        elif choice == "6":
            spinner("Exiting")
            print("\033[95m👋 Goodbye. Stay productive.\033[0m")
            break

        else:
            print("\033[91m❌ Invalid option. Please select 1–6.\033[0m")


if __name__ == "__main__":
    main()
