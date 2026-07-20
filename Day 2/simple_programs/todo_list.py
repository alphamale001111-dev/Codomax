# simple_programs/todo_list.py
"""
Todo List Manager
-----------------
Demonstrates collections (lists & dicts), CRUD operations, iteration,
and conditional control flow in a simple CLI interface.
"""

def show_tasks(tasks):
    print("\n--- Current Tasks ---")
    if not tasks:
        print("[No tasks in your list yet! Add one below]")
        return
        
    for index, task in enumerate(tasks, 1):
        status = "✅ [Completed]" if task["completed"] else "❌ [Pending]"
        print(f"{index}. {task['title']} - {status}")

def main():
    tasks = [] # List of dictionaries: [{"title": "Learn Python", "completed": False}]
    
    print("====================================================")
    print("           📝 PYTHON TODO LIST MANAGER 📝           ")
    print("====================================================")
    
    while True:
        show_tasks(tasks)
        print("\nOptions:")
        print("1. Add a Task")
        print("2. Complete a Task")
        print("3. Delete a Task")
        print("4. Exit")
        
        choice = input("\nSelect an option (1-4): ").strip()
        
        if choice == '1':
            title = input("Enter task description: ").strip()
            if title:
                tasks.append({"title": title, "completed": False})
                print(f"➕ Task '{title}' added successfully!")
            else:
                print("❌ Task description cannot be empty.")
                
        elif choice == '2':
            if not tasks:
                print("❌ No tasks to complete.")
                continue
            show_tasks(tasks)
            try:
                task_num = int(input("\nEnter task number to mark complete: "))
                if 1 <= task_num <= len(tasks):
                    tasks[task_num - 1]["completed"] = True
                    print(f"✅ Marked task {task_num} as complete!")
                else:
                    print("❌ Invalid task number.")
            except ValueError:
                print("❌ Invalid input! Please enter a number.")
                
        elif choice == '3':
            if not tasks:
                print("❌ No tasks to delete.")
                continue
            show_tasks(tasks)
            try:
                task_num = int(input("\nEnter task number to delete: "))
                if 1 <= task_num <= len(tasks):
                    removed = tasks.pop(task_num - 1)
                    print(f"🗑️ Deleted task: '{removed['title']}'")
                else:
                    print("❌ Invalid task number.")
            except ValueError:
                print("❌ Invalid input! Please enter a number.")
                
        elif choice == '4':
            print("\nExiting Todo List. Keep up the productivity! 🚀")
            break
            
        else:
            print("❌ Invalid choice. Please choose between 1 and 4.")

if __name__ == "__main__":
    main()
