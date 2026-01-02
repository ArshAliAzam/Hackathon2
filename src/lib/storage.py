"""
In-Memory Storage Implementation

This module provides in-memory storage for tasks using Python data structures.
"""


class InMemoryStorage:
    """Implements in-memory storage for tasks."""
    
    def __init__(self):
        """Initialize the in-memory storage."""
        self.tasks = {}  # Dictionary to store tasks with ID as key
        self.current_id = 1  # Counter for generating unique IDs
    
    def add_task(self, task):
        """
        Add a task to the storage.
        
        Args:
            task (Task): The task to add
        """
        self.tasks[task.id] = task
    
    def get_task(self, task_id):
        """
        Get a task by its ID.
        
        Args:
            task_id (int): The ID of the task to retrieve
            
        Returns:
            Task: The task with the given ID, or None if not found
        """
        return self.tasks.get(task_id)
    
    def get_all_tasks(self):
        """
        Get all tasks in the storage.
        
        Returns:
            list: A list of all tasks
        """
        return list(self.tasks.values())
    
    def update_task(self, task):
        """
        Update an existing task in the storage.
        
        Args:
            task (Task): The updated task
        """
        if task.id in self.tasks:
            self.tasks[task.id] = task
        else:
            raise ValueError(f"Task with ID {task.id} does not exist")
    
    def delete_task(self, task_id):
        """
        Delete a task by its ID.
        
        Args:
            task_id (int): The ID of the task to delete
        """
        if task_id in self.tasks:
            del self.tasks[task_id]
        else:
            raise ValueError(f"Task with ID {task_id} does not exist")
    
    def get_next_id(self):
        """
        Get the next available ID for a new task.
        
        Returns:
            int: The next available ID
        """
        next_id = self.current_id
        self.current_id += 1
        return next_id