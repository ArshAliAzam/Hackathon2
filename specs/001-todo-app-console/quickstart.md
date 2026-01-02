# Quickstart Guide: Todo In-Memory Python Console App

## Running the Application

To run the todo application, execute the following command from the project root:

```bash
python src/cli/main.py [command] [options]
```

## Available Commands

### Add a Task
```bash
python src/cli/main.py add --title "Task Title" --description "Optional description"
```

### View All Tasks
```bash
python src/cli/main.py list
```

### Update Task Status
```bash
python src/cli/main.py update-status --id 1 --status complete
```
or
```bash
python src/cli/main.py update-status --id 1 --status incomplete
```

### Update Task Details
```bash
python src/cli/main.py update-task --id 1 --title "New Title" --description "New Description"
```

### Delete a Task
```bash
python src/cli/main.py delete --id 1
```

## Example Usage

1. Add a new task:
```bash
python src/cli/main.py add --title "Buy groceries" --description "Milk, bread, eggs"
```

2. View all tasks:
```bash
python src/cli/main.py list
```

3. Mark a task as complete:
```bash
python src/cli/main.py update-status --id 1 --status complete
```

4. Delete a task:
```bash
python src/cli/main.py delete --id 1
```

## Error Handling

The application will display appropriate error messages when:
- Attempting operations on non-existent tasks
- Providing invalid command inputs
- Missing required parameters