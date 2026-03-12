tasks = []

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added!")
    elif choice == "2":
        if not tasks:
            print("No tasks to view!")
        else:
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
    elif choice == "3":
        if not tasks:
            print("No tasks to remove!")
        else:
            task = int(input("Which task to remove?: "))
            if 1 <= task <= len(tasks):
                tasks.pop(task-1)
                print("Task Removed.")
            else:
                print("Invalid task number!")
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid input!")
