import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    if st.session_state["input_todo"] != "":
        new_todo = st.session_state["input_todo"] + "\n"
        todos.append(new_todo)
        functions.write_todos(todos)

        st.session_state["input_todo"] = ""
    else:
        st.warning("Please enter todo to add!")


st.title("My Todo App")
st.subheader("This is my Todo app.")

st.text_input(label="", placeholder="Add new todo...",
              on_change=add_todo, key="input_todo")

for index, todo in enumerate(todos):
    chk_box = st.checkbox(todo, key=f"checkbox_{index}")
    if chk_box:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[f"checkbox_{index}"]
        st.rerun()
