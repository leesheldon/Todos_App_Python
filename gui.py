import functions
import PySimpleGUI as Sg

label = Sg.Text("Type in a to-do")
input_box = Sg.InputText(tooltip="Enter to-do", key="todo")
add_button = Sg.Button("Add")
list_box = Sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=(45, 10))
edit_button = Sg.Button("Edit")
complete_button = Sg.Button("Complete")
exit_button = Sg.Button("Exit")

window = Sg.Window('My To-Do App',
                   layout=[[label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=('Helvetica', 16))

while True:
    event, values = window.read()
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)

            # Update added item in list box
            window['todos'].update(values=todos)
            # Update input box to empty
            window['todo'].update(value='')

        case "Edit":
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)

            # Update edited item in list box
            window['todos'].update(values=todos)
            # Update input box to empty
            window['todo'].update(value='')

        case "Complete":
            todo_to_complete = values['todos'][0]

            todos = functions.get_todos()
            todos.remove(todo_to_complete)
            functions.write_todos(todos)

            # Update Todos list in list box after completed item
            window['todos'].update(values=todos)
            # Update input box to empty
            window['todo'].update(value='')

        case "Exit":
            break
        case 'todos':
            # This event occurred once user select item in list box.

            # Update user selecting item in list box to input box
            window['todo'].update(value=values['todos'][0])
        case Sg.WIN_CLOSED:
            break


window.close()
