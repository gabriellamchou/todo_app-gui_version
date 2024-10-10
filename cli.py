# from functions import get_todos, write_todos
import functions
import time

possible_orders = ["add [task]",
                   "edit [task number]",
                   "complete [task number]",
                   "show",
                   "exit",
                   "help"]

now = time.strftime("%b %d, %Y %H:%M:%S")

print("It is", now)

print("Type 'help' to see list of possible orders")

while True:
    user_order = input("Enter an order: ").strip().lower()
    if user_order.startswith("add "):
        # Use list slicing to get the new task
        task = user_order[4:] + '\n'
        # Store items in todos.txt in a variable
        todos = functions.get_todos()
        # Store new task in todos variable
        todos.append(task)
        # Overwrite todos.txt with new task included
        functions.write_todos(todos)
        print("Task added!")
    elif user_order.startswith("edit "):
        try:
            old_task = user_order[5:]
            old_task = int(old_task) - 1

            todos = functions.get_todos()
            if todos[old_task] not in todos:
                print("The number specified does not correspond with any task")
                continue
            todos[old_task] = input("Enter the new task: ") + '\n'

            functions.write_todos(todos)
            print("The task has been edited successfully!")
        except ValueError:
            print("Invalid command. "
                  "You must specify the number of the task you want to edit.")
            continue
    elif user_order.startswith("complete "):
        try:
            completed_idx = user_order[9:]
            completed_idx = int(completed_idx) - 1

            todos = functions.get_todos()
            completed_todo = todos.pop(completed_idx)

            functions.write_todos(todos)
            print("The task has been completed!")
        except ValueError:
            print("Invalid command. "
                  "You must specify the number of "
                  "the task you want to complete.")
            continue
        except IndexError:
            print("The number specified does not correspond with any task")
            continue
    elif user_order.startswith("show"):
        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            print(f"{index + 1}. {item.capitalize()}")
    elif user_order.startswith("exit"):
        break
    elif user_order.startswith("help"):
        print("Possible orders:")
        for order in possible_orders:
            print(f"  {order}")
    else:
        print("Order not found. Please try again")

print("Program Terminated!")
