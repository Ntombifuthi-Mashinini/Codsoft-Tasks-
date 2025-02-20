import json
from datetime import datetime

in_memory_tasks = []

def load_tasks():
    return in_memory_tasks

def save_tasks(tasks):
    global in_memory_tasks
    in_memory_tasks = tasks
