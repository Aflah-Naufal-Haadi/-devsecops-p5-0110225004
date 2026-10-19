from data import load_tasks, save_tasks
from validation import valid_title, valid_id


def add_task(title):
    if not valid_title(title):
        raise ValueError("Judul wajib diisi, maksimal 100 karakter.")

    tasks = load_tasks()
    next_id = max(
        (task["id"] for task in tasks),
        default=0
    ) + 1

    task = {
        "id": next_id,
        "title": title.strip(),
        "completed": False,
    }

    tasks.append(task)
    save_tasks(tasks)
    return task


def get_tasks():
    return load_tasks()


def finish_task(task_id):
    if not valid_id(task_id):
        raise ValueError("ID harus berupa angka positif.")

    tasks = load_tasks()

    for task in tasks:
        if task["id"] == int(task_id):
            task["completed"] = True
            save_tasks(tasks)
            return task

    raise ValueError("Tugas tidak ditemukan.")