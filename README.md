# Phase 1: In-Memory Python Todo App

## Description
Yeh ek simple CLI-based Todo application hai jo Python mein likhi gayi hai. Yeh in-memory storage use karti hai (Python list).

## Features
1. **Add Task** - Nayi task add karo
2. **List Tasks** - Saari tasks dekho
3. **Mark as Done** - Task ko complete mark karo
4. **Delete Task** - Task ko delete karo
5. **Input Validation** - Empty inputs aur wrong IDs handle karti hai

## Requirements
- Python 3.6 ya usse upar ki version

## Project Structure
```
Phase1/
├── CLAUDE.md          # Project constitution (Spec-Driven Development)
├── README.md          # This file
├── specs/             # Feature specifications
│   └── phase1.md     # Phase 1 requirements
└── src/              # Source code
    └── todo_app.py   # Main application
```

## Kaise Run Karein

### Step 1: Check Python Installation
```bash
python --version
```
Ya
```bash
python3 --version
```

### Step 2: Run the Application
```bash
python src/todo_app.py
```
Ya
```bash
python3 src/todo_app.py
```

## Usage Instructions

Application run karne ke baad aapko menu dikhega:

1. **Option 1** - Add Task
   - Task ka description enter karo
   - Empty description allowed nahi hai

2. **Option 2** - List Tasks
   - Saari tasks ID, Status, aur Description ke saath dikhegi

3. **Option 3** - Mark Task as Done
   - Pehle saari tasks dikhegi
   - Task ID enter karo jise done mark karna hai

4. **Option 4** - Delete Task
   - Pehle saari tasks dikhegi
   - Task ID enter karo jise delete karna hai

5. **Option 5** - Exit
   - Application se exit karo

## Example Session
```
Welcome to Python Console Todo App!

============================================================
         Python Console Todo App - Phase 1
============================================================
1. Add Task
2. List Tasks
3. Mark Task as Done
4. Delete Task
5. Exit
============================================================

Enter your choice (1-5): 1
Enter task description: Complete Python assignment
Task added successfully! (ID: 1)

Enter your choice (1-5): 2

============================================================
ID    Status     Description
============================================================
1     ○ Pending  Complete Python assignment
============================================================
```

## Error Handling
- Empty task description nahi add ho sakta
- Invalid task ID error deta hai
- Wrong menu choice validate hota hai
- Non-numeric IDs handle hoti hain

## Technical Details
- **Storage**: In-memory Python list
- **Data Structure**: Dictionary-based tasks with ID, description, and done status
- **ID Management**: Auto-incrementing IDs

## Notes
- Yeh application in-memory hai, matlab jab app close hoga toh data save nahi rahega
- Aglay phases mein persistent storage add hoga
