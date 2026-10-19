def valid_title(title):
    return isinstance(title, str) and 0 < len(title.strip()) <= 100


def valid_id(task_id):
    try:
        return int(task_id) > 0
    except (ValueError, TypeError):
        return False