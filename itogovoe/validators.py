ALLOWED_PRIORITIES = {"low", "normal", "high"}


def validate_task_data(data: dict):
    if not isinstance(data, dict):
        raise ValueError("Invalid JSON body")

    if "title" not in data:
        raise ValueError("Missing field: title")

    if not isinstance(data["title"], str) or not data["title"].strip():
        raise ValueError("Field 'title' must be a non-empty string")

    if "priority" not in data:
        raise ValueError("Missing field: priority")

    if not isinstance(data["priority"], str):
        raise ValueError("Field 'priority' must be a string")

    if data["priority"] not in ALLOWED_PRIORITIES:
        raise ValueError("Invalid priority value")
