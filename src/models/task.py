"""
Task Model

This module defines the Task entity with its attributes and methods.
"""


class Task:
    """Represents a single task in the todo list."""
    
    def __init__(self, id, title, description=None, completed=False):
        """
        Initialize a new Task.
        
        Args:
            id (int): Unique identifier for the task
            title (str): Task title
            description (str, optional): Task description
            completed (bool): Completion status of the task
        """
        if not isinstance(id, int):
            raise ValueError("Task ID must be an integer")
        
        if not title or not title.strip():
            raise ValueError("Task title cannot be empty")
        
        if not isinstance(completed, bool):
            raise ValueError("Task completion status must be a boolean")
        
        self.id = id
        self.title = title.strip()
        self.description = description.strip() if description else None
        self.completed = completed
    
    def __str__(self):
        """Return a string representation of the task."""
        status = "Completed" if self.completed else "Pending"
        return f"Task {self.id}: {self.title} [{status}]"
    
    def __repr__(self):
        """Return a detailed string representation of the task."""
        return f"Task(id={self.id}, title='{self.title}', description='{self.description}', completed={self.completed})"
    
    def to_dict(self):
        """Convert the task to a dictionary representation."""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "completed": self.completed
        }
    
    @classmethod
    def from_dict(cls, data):
        """Create a Task instance from a dictionary."""
        return cls(
            id=data["id"],
            title=data["title"],
            description=data.get("description"),
            completed=data.get("completed", False)
        )