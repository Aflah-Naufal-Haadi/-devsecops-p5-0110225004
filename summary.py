def task_summary(tasks):
    total = len(tasks)
    completed = sum(
        1 for task in tasks if task.get("completed") is True
    )

    return {
        "total": total,
        "completed": completed,
        "pending": total - completed,
    }