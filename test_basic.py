"""
Basic test to verify the todo application works as expected.
"""

import sys
import os

# Add the src directory to the path so we can import our modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from src.models.task import Task
from src.lib.storage import InMemoryStorage
from src.services.task_manager import TaskManager


def test_task_creation():
    """Test that tasks can be created properly."""
    print("Testing task creation...")
    
    # Test basic task creation
    task = Task(1, "Test Task", "This is a test task")
    assert task.id == 1
    assert task.title == "Test Task"
    assert task.description == "This is a test task"
    assert task.completed == False
    
    # Test task creation with completion status
    task2 = Task(2, "Another Task", "Another description", True)
    assert task2.completed == True
    
    # Test task creation without description
    task3 = Task(3, "No Description Task")
    assert task3.description is None
    
    print("PASS: Task creation tests passed")


def test_in_memory_storage():
    """Test that in-memory storage works properly."""
    print("Testing in-memory storage...")
    
    storage = InMemoryStorage()
    
    # Test adding a task
    task = Task(1, "Test Task", "Description")
    storage.add_task(task)
    
    # Test retrieving the task
    retrieved_task = storage.get_task(1)
    assert retrieved_task is not None
    assert retrieved_task.id == 1
    assert retrieved_task.title == "Test Task"
    
    # Test getting all tasks
    all_tasks = storage.get_all_tasks()
    assert len(all_tasks) == 1
    assert all_tasks[0].id == 1
    
    # Test updating a task
    retrieved_task.title = "Updated Title"
    storage.update_task(retrieved_task)
    
    updated_task = storage.get_task(1)
    assert updated_task.title == "Updated Title"
    
    # Test deleting a task
    storage.delete_task(1)
    deleted_task = storage.get_task(1)
    assert deleted_task is None
    
    # Test ID generation
    next_id = storage.get_next_id()
    assert next_id == 1  # First ID should be 1

    # Test that the next ID is incremented
    next_id2 = storage.get_next_id()
    assert next_id2 == 2  # Second ID should be 2

    print("PASS: In-memory storage tests passed")


def test_task_manager():
    """Test that the task manager works properly."""
    print("Testing task manager...")
    
    manager = TaskManager()
    
    # Test adding a task
    task = manager.add_task("Test Task", "Test Description")
    assert task.id == 1
    assert task.title == "Test Task"
    assert task.description == "Test Description"
    assert task.completed == False
    
    # Test listing tasks
    tasks = manager.list_tasks()
    assert len(tasks) == 1
    assert tasks[0].id == 1
    
    # Test updating task status
    manager.update_task_status(1, True)
    task = manager.get_task(1)
    assert task.completed == True
    
    # Test updating task details
    manager.update_task_details(1, "Updated Title", "Updated Description")
    task = manager.get_task(1)
    assert task.title == "Updated Title"
    assert task.description == "Updated Description"
    
    # Test deleting task
    manager.delete_task(1)
    tasks = manager.list_tasks()
    assert len(tasks) == 0
    
    print("PASS: Task manager tests passed")


def run_all_tests():
    """Run all tests."""
    print("Running basic tests for the Todo Console Application...\n")
    
    test_task_creation()
    test_in_memory_storage()
    test_task_manager()
    
    print("\nAll tests passed! The application is working correctly.")


if __name__ == "__main__":
    run_all_tests()