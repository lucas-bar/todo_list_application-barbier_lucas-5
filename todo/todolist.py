# todolist.py
class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, title):
        task = Task(title)
        self.tasks.append(task)

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]

    def display_tasks(self):
        for index, task in enumerate(self.tasks):
            print(f"{index + 1}. {task}")
