"""
Task Manager Service

This module contains the business logic for managing tasks.
It handles creating, reading, updating, and deleting tasks.
"""

from src.models.task import Task
from src.lib.storage import InMemoryStorage


class TaskManager:
    """Manages tasks using in-memory storage."""
    
    def __init__(self):
        """Initialize the task manager with in-memory storage."""
        self.storage = InMemoryStorage()
    
    def add_task(self, title, description=None):
        """Add a new task with the given title and optional description."""
        if not title or not title.strip():
            raise ValueError("Task title cannot be empty")
        
        task_id = self.storage.get_next_id()
        task = Task(task_id, title.strip(), description.strip() if description else None)
        self.storage.add_task(task)
        return task
    
    def list_tasks(self):
        """Return a list of all tasks."""
        return self.storage.get_all_tasks()
    
    def get_task(self, task_id):
        """Get a specific task by its ID."""
        return self.storage.get_task(task_id)
    
    def update_task_status(self, task_id, completed):
        """Update the completion status of a task."""
        task = self.get_task(task_id)
        if not task:
            raise ValueError(f"Task with ID {task_id} does not exist")
        
        task.completed = completed
        self.storage.update_task(task)
        return task
    
    def update_task_details(self, task_id, title=None, description=None):
        """Update the title or description of a task."""
        task = self.get_task(task_id)
        if not task:
            raise ValueError(f"Task with ID {task_id} does not exist")
        
        if title is not None:
            if not title.strip():
                raise ValueError("Task title cannot be empty")
            task.title = title.strip()
        
        if description is not None:
            task.description = description.strip() if description.strip() else None
        
        self.storage.update_task(task)
        return task
    
    def delete_task(self, task_id):
        """Delete a task by its ID."""
        task = self.get_task(task_id)
        if not task:
            raise ValueError(f"Task with ID {task_id} does not exist")
        
        self.storage.delete_task(task_id)