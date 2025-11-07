# todo.py - Console-based To-Do List App (Persistent Storage)

TASK_FILE = "tasks.txt"

def load_tasks():
    try:
        with open(TASK_FILE, "r") as file:
            tasks = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        tasks = []
    return tasks

def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def add_task(task):
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print(f"✅ Task added: {task}")

def remove_task(task_index):
    tasks = load_tasks()
    try:
        removed = tasks.pop(task_index - 1)
        save_tasks(tasks)
        print(f"🗑️ Task removed: {removed}")
    except IndexError:
        print("⚠ Invalid task number.")

def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("📭 Your to-do list is empty.")
    else:
        print("\n📝 Your Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def main():
    while True:
        print("\n==== TO-DO LIST MENU ====")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            view_tasks()
        elif choice == "2":
            task = input("Enter task: ").strip()
            add_task(task)
        elif choice == "3":
            view_tasks()
            try:
                task_num = int(input("Enter task number to remove: "))
                remove_task(task_num)
            except ValueError:
                print("⚠ Please enter a valid number.")
        elif choice == "4":
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("⚠ Invalid choice. Try Again.")

if __name__ == "__main__":
    main()
