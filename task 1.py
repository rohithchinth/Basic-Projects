class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})

    def complete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]["completed"] = True
        else:
            print("Invalid task index!")

    def remove_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            del self.tasks[task_index]
        else:
            print("Invalid task index!")

    def show_tasks(self):
        if self.tasks:
            print("Tasks:")
            for i, task in enumerate(self.tasks):
                status = "Completed" if task["completed"] else "Not Completed"
                print(f"{i + 1}. {task['task']} - {status}")
        else:
            print("No tasks added yet.")

def main():
    manager = TaskManager()

    while True:
        print("\nTask Manager Menu:")
        print("1. Add Task")
        print("2. Complete Task")
        print("3. Remove Task")
        print("4. Show Tasks")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter task: ")
            manager.add_task(task)
        elif choice == "2":
            task_index = int(input("Enter task index to complete: ")) - 1
            manager.complete_task(task_index)
        elif choice == "3":
            task_index = int(input("Enter task index to remove: ")) - 1
            manager.remove_task(task_index)
        elif choice == "4":
            manager.show_tasks()
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Please choose again.")

if __name__ == "__main__":
    main()
