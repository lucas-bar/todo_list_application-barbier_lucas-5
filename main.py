# main.py
from todo.task import Task
from todo.todolist import TodoList

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
