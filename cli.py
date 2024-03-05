from functions import get_todos, write_todos
import time

now = time.strftime("%b %d %Y %H:%M:%S")
print("It is", now)

while True:
    # Get user input and strip space characters from it
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:] + "\n"

        todos = get_todos()

        todos.append(todo)

        write_todos(todos)

    elif user_action.startswith('show'):
        todos = get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = get_todos()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + "\n"

            write_todos(todos)
        except ValueError:
            print("Your command is not valid. --> edit {number of the todo}")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            todos = get_todos()

            index_be_removed = number - 1
            todo_be_removed = todos[index_be_removed].strip('\n')
            todos.pop(index_be_removed)

            write_todos(todos)

            message = f"Todo {todo_be_removed} was removed from the list."
            print(message)
        except ValueError:
            print("Your command is not valid. --> complete {number of the todo}")
            continue
        except IndexError:
            print("Please choose a number from the list.")
            continue

    elif user_action.startswith('exit'):
        break
    else:
        print("Command is not valid.")

print("Bye!")
