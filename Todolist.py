#To-Do List 

todo_list = []

while True:
    print("\n--- To-Do List ---")
    print("1. Add task")
    print("2. Remove task")
    print("3. View tasks")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        task = input("Enter the task to add: ")
        todo_list.append(task)
        print(f"'{task}' added to the list.")
    elif choice == '2':
        task = input("Enter the task to remove: ")
        if task in todo_list:
            todo_list.remove(task)
            print(f"'{task}' removed from the list.")
        else:
            print("Task not found!")
    elif choice == '3':
        print("Your Tasks:")
        for idx, task in enumerate(todo_list, 1):
            print(f"{idx}. {task}")
    elif choice == '4':
        print("Exiting To-Do List.")
        break
    else:
        print("Invalid choice! Please choose 1-4.")
