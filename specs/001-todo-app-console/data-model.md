# Data Model: Todo In-Memory Python Console App

## Task Entity

### Attributes
- **id**: Integer (required) - Unique identifier for the task
- **title**: String (required) - The task title
- **description**: String (optional) - Additional details about the task
- **completed**: Boolean (required) - Completion status of the task (default: False)

### Validation Rules
- ID must be unique across all tasks
- Title must be a non-empty string
- Description can be empty or null
- Completed status must be a boolean value

### State Transitions
- A task can transition from incomplete (False) to complete (True)
- A task can transition from complete (True) back to incomplete (False)

## In-Memory Storage Structure

### Task Storage
- **tasks**: Dictionary where:
  - Key: Integer (task ID)
  - Value: Task object instance

### ID Generation
- **current_id**: Integer counter starting at 1
- Incremented each time a new task is created
- Ensures unique IDs across all tasks

## Relationships
- No relationships needed as this is a single-entity system