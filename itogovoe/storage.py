import json
import os
from task import Task


class TaskStorage:
    def __init__(self, filename: str = "tasks.txt"):
        self.filename = filename
        self.tasks = []
        self.next_id = 1
        self.load()

    def add_task(self, title: str, priority: str) -> Task:
        task = Task(self.next_id, title, priority)
        self.tasks.append(task)
        self.next_id += 1
        self.save()
        return task

    def get_all(self) -> list:
        return self.tasks

    def complete_task(self, task_id: int) -> bool:
        for task in self.tasks:
            if task.id == task_id:
                task.isDone = True
                self.save()
                return True
        return False

    def save(self):
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump([task.to_dict() for task in self.tasks], f, ensure_ascii=False)

    def load(self):
        if not os.path.exists(self.filename):
            return

        with open(self.filename, "r", encoding="utf-8") as f:
            data = json.load(f)
            self.tasks = [Task.from_dict(item) for item in data]

        if self.tasks:
            self.next_id = max(task.id for task in self.tasks) + 1
