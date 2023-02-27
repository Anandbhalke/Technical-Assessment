
# Define two empty lists, todo_list and completed_tasks,
#which will be used to store the user's to-do tasks and completed tasks, respectively.

todo_list = []
completed_tasks = []

# Function to add a new task to the to-do list
def add_task():
    task_description = input("Enter a description of the task: ")
    todo_list.append(task_description)
    print("Task added successfully!")

""""Function add_task() prompts the user to enter a description of a new task,
and then adds it to the end of the todo_list using the append() method,
It then prints a success message to the console.. """


# Function to mark a task as complete and move it to the completed tasks list
def mark_task_complete():
    task_number = int(input("Enter the number of the task you want to mark as complete: "))
    if task_number < 1 or task_number > len(todo_list):
        print("Invalid task number.")
    else:
        task_description = todo_list.pop(task_number - 1)
        completed_tasks.append(task_description)
        print("Task marked as complete and moved to completed tasks list.")

"""Function mark_task_complete() prompts the user to enter the number of a task that they want to mark as complete.
If the task number is not a valid index in the todo_list, the function prints an error message.
Otherwise, it removes the task from todo_list using the pop() method (which removes the item at the specified index and returns it), 
and adds it to the end of completed_tasks using the append() method. It then prints a success message to the console."""




# Function to display the to-do list
def view_todo_list():
    if len(todo_list) == 0:
        print("There are no tasks in the to-do list.")
    else:
        print("To-Do List:")
        for i in range(len(todo_list)):
            print(f"{i+1}. {todo_list[i]}")      

"""Function view_todo_list() checks if todo_list is empty, and if so, prints a message indicating that there are no tasks.
Otherwise, it prints a header indicating that the following list is the to-do list, and then uses a for loop to iterate over the indices of todo_list.
For each index i, it prints a line to the console containing the index number plus one(beacuse Python lists are 0-indexed), 
followed by a dot and the task description at index i"""





# Function to delete a task from the to-do list
def delete_task():
    task_number = int(input("Enter the number of the task you want to delete: "))
    if task_number < 1 or task_number > len(todo_list):
        print("Invalid task number.")
    else:
        todo_list.pop(task_number - 1)
        print("Task deleted successfully.")


"""This function delete_task() prompts the user to enter the number of a task that they want to delete. 
if the task number is not a valid index in the todo_list, the function prints an error message. Otherwise, 
it removes the task from todo_list using the pop() method,
and prints a success message to the console"""


# Main loop to display the menu and perform actions based on user input

while True:
    print("\nMenu:")   #\n (newline) will print a blank line, followed by the word "Menu" on the next line
    print("1. Add a new task")
    print("2. Mark a task as complete")
    print("3. View the to-do list")
    print("4. Delete a task")
    print("5. Exit")

    choice = input("Enter your choice: ")
    if choice == "1":
        add_task()
    elif choice == "2":
        mark_task_complete()
    elif choice == "3":
        view_todo_list()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please try again.")

# while True loop is used to continuously display the menu and perform actions based on user input, 
# until the user chooses to exit the program.


# to run the program, save the code above to a file named "todo_list_manager.py" 
# run it in a Python interpreter by typing python todo_list_manager.py in the command line.