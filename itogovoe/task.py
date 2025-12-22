class Task:
    def __init__(self, task_id: int, title: str, priority: str, is_done: bool = False):
        self.id = task_id
        self.title = title
        self.priority = priority
        self.isDone = is_done

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "title": self.title,
            "priority": self.priority,
            "isDone": self.isDone
        }

    @staticmethod
    def from_dict(data: dict) -> "Task":
        return Task(
            task_id=data["id"],
            title=data["title"],
            priority=data["priority"],
            is_done=data["isDone"]
        )
