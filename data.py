import json
from pathlib import Path

FILE_DATA = Path(__file__).parent / "tasks.json"


def load_tasks():
    if not FILE_DATA.exists():
        return []

    try:
        with FILE_DATA.open("r", encoding="utf-8") as file:
            tasks = json.load(file)

        return tasks if isinstance(tasks, list) else []
    except (json.JSONDecodeError, OSError):
        return []


def save_tasks(tasks):
    with FILE_DATA.open("w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=4, ensure_ascii=False)