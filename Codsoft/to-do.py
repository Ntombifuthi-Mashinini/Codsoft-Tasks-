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

