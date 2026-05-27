def add_task(memory, task):

    memory["tasks"].append(task)

    return f"Task added: {task}"


def show_tasks(memory):

    tasks = memory["tasks"]

    if not tasks:
        return "No active tasks."

    result = ""

    for i, task in enumerate(tasks, start=1):

        result += f"{i}. {task}\n"

    return result