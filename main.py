# main.py
class Task:
    def __init__(self, title, completed=False):
        self.title = title
        self.completed = completed

    def mark_as_completed(self):
        self.completed = True

    def __str__(self):
        return f"{'[X]' if self.completed else '[ ]'} {self.title}"


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


def main():
    todo_list = TodoList()

    while True:
        print("\nTodo List:")
        todo_list.display_tasks()

        print("\nMenu:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter task title: ")
            todo_list.add_task(title)
        elif choice == "2":
            index = int(input("Enter task index to remove: ")) - 1
            todo_list.remove_task(index)
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
