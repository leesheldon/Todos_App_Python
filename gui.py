import functions
import PySimpleGUI as Sg
import time

Sg.theme("LightBrown3")

clock_label = Sg.Text("", key="clock")
label = Sg.Text("Type in a to-do")
input_box = Sg.InputText(tooltip="Enter to-do", key="todo")
add_button = Sg.Button("Add")
list_box = Sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=(45, 10))
edit_button = Sg.Button("Edit")
complete_button = Sg.Button("Complete")
exit_button = Sg.Button("Exit")

window = Sg.Window('My To-Do App',
                   layout=[[clock_label],
                           [label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=('Helvetica', 16))

while True:
    event, values = window.read(timeout=1000)
    window["clock"].update(value=time.strftime("%b %d %Y %H:%M:%S"))

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
            try:
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
            except IndexError:
                Sg.popup("Please select an to-do item first!",
                         font=('Helvetica', 16))

        case "Complete":
            try:
                todo_to_complete = values['todos'][0]

                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)

                # Update Todos list in list box after completed item
                window['todos'].update(values=todos)
                # Update input box to empty
                window['todo'].update(value='')
            except IndexError:
                Sg.popup("Please select an to-do item first!",
                         font=('Helvetica', 16))

        case "Exit":
            break
        case 'todos':
            # This event occurred once user select item in list box.

            # Update user selecting item in list box to input box
            window['todo'].update(value=values['todos'][0])
        case Sg.WIN_CLOSED:
            break


window.close()
