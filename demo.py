"""
Demo script to show the functionality of the Todo Console Application.
This script demonstrates all the main features in a single run.
"""

import sys
import os

# Add the src directory to the path so we can import our modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '.'))

from src.services.task_manager import TaskManager


def demo():
    """Demonstrate the functionality of the todo application."""
    print("Todo Console Application Demo")
    print("=" * 40)
    
    # Initialize the task manager
    task_manager = TaskManager()
    
    # Add some tasks
    print("\n1. Adding tasks:")
    task1 = task_manager.add_task("Buy groceries", "Milk, bread, eggs")
    print(f"   Added task: {task1.title} (ID: {task1.id})")
    
    task2 = task_manager.add_task("Complete project", "Finish the implementation")
    print(f"   Added task: {task2.title} (ID: {task2.id})")
    
    task3 = task_manager.add_task("Call mom")
    print(f"   Added task: {task3.title} (ID: {task3.id})")
    
    # List all tasks
    print("\n2. Listing all tasks:")
    tasks = task_manager.list_tasks()
    for task in tasks:
        status = "[X]" if task.completed else "[ ]"
        desc = task.description if task.description else "No description"
        print(f"   {status} [{task.id}] {task.title}")
        print(f"       Description: {desc}")
    
    # Update task status
    print(f"\n3. Updating task {task.id} status to complete:")
    task_manager.update_task_status(task1.id, True)
    updated_task = task_manager.get_task(task1.id)
    print(f"   Task {updated_task.id} is now {'completed' if updated_task.completed else 'incomplete'}")
    
    # Update task details
    print(f"\n4. Updating task {task2.id} details:")
    task_manager.update_task_details(task2.id, "Complete project proposal", "Finish and submit the project proposal")
    updated_task2 = task_manager.get_task(task2.id)
    print(f"   Updated task {updated_task2.id}:")
    print(f"     Title: {updated_task2.title}")
    print(f"     Description: {updated_task2.description}")
    
    # List all tasks again to see changes
    print("\n5. Listing all tasks after updates:")
    tasks = task_manager.list_tasks()
    for task in tasks:
        status = "[X]" if task.completed else "[ ]"
        desc = task.description if task.description else "No description"
        print(f"   {status} [{task.id}] {task.title}")
        print(f"       Description: {desc}")
    
    # Delete a task
    print(f"\n6. Deleting task {task3.id}:")
    task_manager.delete_task(task3.id)
    print(f"   Task {task3.id} deleted")
    
    # List all tasks after deletion
    print("\n7. Listing all tasks after deletion:")
    tasks = task_manager.list_tasks()
    if not tasks:
        print("   No tasks found.")
    else:
        for task in tasks:
            status = "[X]" if task.completed else "[ ]"
            desc = task.description if task.description else "No description"
            print(f"   {status} [{task.id}] {task.title}")
            print(f"       Description: {desc}")
    
    print("\nDemo completed successfully!")


if __name__ == "__main__":
    demo()