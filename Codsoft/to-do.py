import json
from datetime import datetime

in_memory_tasks = []

def load_tasks():
    return in_memory_tasks

def save_tasks(tasks):
    global in_memory_tasks
    in_memory_tasks = tasks

    def show_tasks(tasks):
    if not tasks:
        print("No tasks available. Add a new task!")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, 1):
            status = "[✓]" if task["completed"] else "[ ]"
            priority = task.get("priority", "None")
            category = task.get("category", "General")
            due_date = task.get("due_date", "No due date")
            
            overdue = "(Overdue!)" if not task["completed"] and task.get("due_date") and datetime.strptime(task["due_date"], "%Y-%m-%d") < datetime.now() else ""
            
            print(f"{i}. {status} {task['title']} (Priority: {priority}, Category: {category}, Due: {due_date}) {overdue}")
        
        show_progress(tasks)

        def show_progress(tasks):
    total = len(tasks)
    completed = sum(1 for task in tasks if task["completed"])
    print(f"\nProgress: {completed}/{total} tasks completed")

    def add_task(tasks):
    title = input("Enter the task: ").strip()
    priority = input("Set priority (High/Medium/Low): ").strip().capitalize()
    category = input("Enter category (e.g., Work, Home): ").strip().capitalize()
    due_date = input("Enter due date (YYYY-MM-DD, optional): ").strip()

    new_task = {
        "title": title,
        "completed": False,
        "priority": priority if priority in ["High", "Medium", "Low"] else "Medium",
        "category": category if category else "General",
        "due_date": due_date if due_date else "No due date"
    }

    tasks.append(new_task)
    print("Task added successfully!")



