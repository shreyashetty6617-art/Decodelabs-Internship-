tasks = []
while True:
    print("\n--- To-Do List ---")
    print("1. Add task")
    print("2. View tasks")
    print("3. Remove task")
    print("4. Exit")

    choice = input("Enter choice (1-4): ")

    if choice == "1":
        task = input("Enter your task: ")
        tasks.append(task)
        print(f"Added: {task}")

    elif choice == "2":
        print("\nYour tasks:")
        if len(tasks) == 0:
            print("No tasks yet!")
        else:
            for i, t in enumerate(tasks, 1):
                print(f"{i}. {t}")

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to remove!")
        else:
            num = int(input("Enter task number to remove: "))
            removed = tasks.pop(num-1)
            print(f"Removed: {removed}")

    elif choice == "4":
        print("Bye! Project completed.")
        break

    else:
        print("Invalid choice! Enter 1-4")


    
    
