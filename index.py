# User Interface (UI):
# Create a command-line interface (CLI) for the To-Do List Application.
# Display a welcoming message and a menu with the following options:
# Welcome to the To-Do List App!

# Menu:
# 1. Add a task
# 2. View tasks
# 3. Mark a task as complete
# 4. Delete a task
# 5. Quit
# To-Do List Features:
# Implement the following features for the To-Do List:
# Adding a task 
# Viewing the list of tasks
# Deleting a task.
# Quitting the application.

tasks=[]

def add_task():
    task= input("Please enter a task: ")
    tasks.append(task)
    print(f"Task'{task}' added to the list")

def view_task():
    if not tasks:
        print("There are no tasks currently")
    else:
        print("Current Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"Task #{index}. {task}")



def delete_task():
    view_task()
    try:
        task_to_delete= int(input("Choose a task to delete: "))
        if task_to_delete >=0 and task_to_delete <len(tasks):
            tasks.pop(task_to_delete)
            print(f"Task {task_to_delete} has been removed")

        else:
            print(f"Task #{task_to_delete} was not found.")
    except:
        print("Invalid input")

def completed_task():
    if tasks:
        print("Mark a task as complete:")
        for index, task in enumerate(tasks, start=1):
            print




if __name__ == "__main__":
    print("Welcom to the To-Do List application :)")
    while True:  
        print("\n")
        print('Please select one of the following options:')
        print("--------------------------------------")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Mark a task as complete")
        print("4. Delete a task")
        print("5. Quit")
        
        choice = input("Enter your choice (1-4): ")
        if choice == '1':
            add_task()
        elif choice =='2':
            view_task()
        elif choice =='3':
            completed_task()
        elif choice =='4':
            delete_task()
        elif choice =='4':
            break
        else:
            print("Invalid Input! Please try again")
        
    print("Good-bye👋🏽👋🏽")