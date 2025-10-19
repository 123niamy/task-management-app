from manager import TaskManager

def main():
    manager = TaskManager()
    while True:
        print("\n1. Add Task\n2. List Tasks\n3. Mark Complete\n4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Title: ")
            description = input("Description: ")
            due_date = input("Due Date (YYYY-MM-DD): ")
            priority = input("Priority (Low/Medium/High): ")
            manager.add_task(title, description, due_date, priority)

        elif choice == "2":
            manager.list_tasks()

        elif choice == "3":
            task_id = int(input("Enter task ID to mark complete: "))
            if manager.mark_complete(task_id):
                print("Task marked as complete.")
            else:
                print("Task not found.")

        elif choice == "4":
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
