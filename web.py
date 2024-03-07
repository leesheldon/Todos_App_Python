import streamlit as st
import functions


todos = functions.get_todos()


def add_todo():
    new_todo = st.session_state["input_todo"] + "\n"
    todos.append(new_todo)
    functions.write_todos(todos)


st.title("My Todo App")
st.subheader("This is my Todo app.")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Add new todo...",
              on_change=add_todo, key="input_todo")






















