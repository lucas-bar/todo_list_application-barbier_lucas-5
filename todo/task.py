# task.py
class Task:
    def __init__(self, title, completed=False):
        self.title = title
        self.completed = completed

    def mark_as_completed(self):
        self.completed = True

    def __str__(self):
        return f"{'[X]' if self.completed else '[ ]'} {self.title}"
