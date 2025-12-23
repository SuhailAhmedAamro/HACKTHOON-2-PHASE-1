#!/usr/bin/env python3
"""
Phase 1: In-Memory Python Todo App
A simple CLI-based todo application using in-memory storage
"""

class TodoApp:
    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def add_task(self, description):
        """Add a new task to the list"""
        if not description or description.strip() == "":
            print("Error: Task description cannot be empty!")
            return False

        task = {
            'id': self.next_id,
            'description': description.strip(),
            'done': False
        }
        self.tasks.append(task)
        self.next_id += 1
        print(f"Task added successfully! (ID: {task['id']})")
        return True

    def list_tasks(self):
        """Display all tasks"""
        if not self.tasks:
            print("\nNo tasks found. Your todo list is empty!")
            return

        print("\n" + "="*60)
        print(f"{'ID':<5} {'Status':<10} {'Description'}")
        print("="*60)

        for task in self.tasks:
            status = "✓ Done" if task['done'] else "○ Pending"
            print(f"{task['id']:<5} {status:<10} {task['description']}")

        print("="*60)

    def mark_done(self, task_id):
        """Mark a task as done"""
        try:
            task_id = int(task_id)
        except ValueError:
            print("Error: Task ID must be a number!")
            return False

        for task in self.tasks:
            if task['id'] == task_id:
                if task['done']:
                    print(f"Task {task_id} is already marked as done!")
                else:
                    task['done'] = True
                    print(f"Task {task_id} marked as done!")
                return True

        print(f"Error: Task with ID {task_id} not found!")
        return False

    def delete_task(self, task_id):
        """Delete a task from the list"""
        try:
            task_id = int(task_id)
        except ValueError:
            print("Error: Task ID must be a number!")
            return False

        for i, task in enumerate(self.tasks):
            if task['id'] == task_id:
                deleted_task = self.tasks.pop(i)
                print(f"Task {task_id} deleted: '{deleted_task['description']}'")
                return True

        print(f"Error: Task with ID {task_id} not found!")
        return False

    def show_menu(self):
        """Display the main menu"""
        print("\n" + "="*60)
        print("         Python Console Todo App - Phase 1")
        print("="*60)
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")
        print("="*60)

    def run(self):
        """Main application loop"""
        print("\nWelcome to Python Console Todo App!")

        while True:
            self.show_menu()
            choice = input("\nEnter your choice (1-5): ").strip()

            if choice == '1':
                description = input("Enter task description: ")
                self.add_task(description)

            elif choice == '2':
                self.list_tasks()

            elif choice == '3':
                self.list_tasks()
                if self.tasks:
                    task_id = input("\nEnter task ID to mark as done: ")
                    self.mark_done(task_id)

            elif choice == '4':
                self.list_tasks()
                if self.tasks:
                    task_id = input("\nEnter task ID to delete: ")
                    self.delete_task(task_id)

            elif choice == '5':
                print("\nThank you for using Todo App! Goodbye!")
                break

            else:
                print("\nError: Invalid choice! Please enter a number between 1-5.")


def main():
    app = TodoApp()
    app.run()


if __name__ == "__main__":
    main()
