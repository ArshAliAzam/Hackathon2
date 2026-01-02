# API Contract: Todo In-Memory Python Console App

## Command Structure

The application accepts commands via command-line arguments using the following structure:

```
python src/cli/main.py <command> [options]
```

## Commands and Options

### 1. Add Task
- **Command**: `add`
- **Options**:
  - `--title` (required): String - The task title
  - `--description` (optional): String - The task description
- **Response**: Success message with assigned task ID or error message

### 2. List Tasks
- **Command**: `list`
- **Options**: None
- **Response**: Formatted list of all tasks with ID, title, description, and completion status, or message indicating empty list

### 3. Update Task Status
- **Command**: `update-status`
- **Options**:
  - `--id` (required): Integer - The task ID
  - `--status` (required): String - Either "complete" or "incomplete"
- **Response**: Success confirmation or error message

### 4. Update Task Details
- **Command**: `update-task`
- **Options**:
  - `--id` (required): Integer - The task ID
  - `--title` (optional): String - New task title
  - `--description` (optional): String - New task description
- **Response**: Success confirmation or error message

### 5. Delete Task
- **Command**: `delete`
- **Options**:
  - `--id` (required): Integer - The task ID
- **Response**: Success confirmation or error message

## Error Handling Contract

All commands will return appropriate error messages when:
- Invalid or missing parameters are provided
- Operations are attempted on non-existent tasks
- Invalid status values are provided

## Success Criteria
- All commands execute in under 1 second
- Clear, user-friendly output for all operations
- Proper error messages for invalid operations